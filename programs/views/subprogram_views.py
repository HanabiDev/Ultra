#encoding: utf-8
from functools import partial
from io import BytesIO

from django.db.models import Sum, F

from django.http.response import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus.doctemplate import SimpleDocTemplate, BaseDocTemplate, PageTemplate
from reportlab.platypus.flowables import PageBreak
from reportlab.platypus.frames import Frame
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.tables import Table, TableStyle

from athletes.views import permissions
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy

from contractors.models import AppUser, BeneficiaryCategory, Intervention
from programs.models import Program, Subprogram
from programs.forms import SubprogramForm
from reports.pdf_test import styleH2, styleN, styleH2E, styleH, BreakdownPieDrawing, header, styleNC
from reports.plot_types import GroupedBarChart


@login_required(login_url='login')
@user_passes_test(permissions, login_url='login')
def list_subprograms(request):
    subprograms = Subprogram.objects.all()
    return render(request, 'subprograms_list.html', {'subprograms':subprograms})

@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_subprogram(request, program_id=None):

    if request.method == 'GET':
        form = None
        if program_id:
            program = Program.objects.get(id=program_id)
            form = SubprogramForm(initial={'program': program})
        else:
            form = SubprogramForm()
        return render(request, 'subprogram.html', {'form': form})

    if request.method == 'POST':
        form = SubprogramForm(request.POST)

        if form.is_valid():
            new_subprogram = form.save()
            if program_id:
                return redirect(reverse_lazy('programs:view_program', kwargs={'program_id': str(program_id)}))

            return redirect(reverse_lazy('subprograms:view_subprogram', kwargs={'subprogram_id': str(new_subprogram.id)}))

        return render(request, 'subprogram.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def view_subprogram(request, subprogram_id):
    subprogram = Subprogram.objects.get(id=subprogram_id)
    return render(request, 'subprogram_detail.html', {'subprogram': subprogram})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def view_map(request, subprogram_id):
    subprogram = Subprogram.objects.get(id=subprogram_id)
    interventions = subprogram.intervention_set.all()
    return render(request, 'program_map.html', {'intervs': interventions})




@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def update_subprogram(request, subprogram_id):

    subprogram = Subprogram.objects.get(id=subprogram_id)
    if request.method == 'GET':
        form = SubprogramForm(instance=subprogram)
        return render(request, 'subprogram.html', {'subprogram':subprogram, 'form': form, 'editing': True})

    if request.method == 'POST':
        form = SubprogramForm(request.POST, request.FILES, instance=subprogram)

        if form.is_valid():
            subprogram = form.save()
            return redirect(reverse_lazy('subprograms:view_subprogram', kwargs={'subprogram_id': str(subprogram.id)}))

        return render(request, 'subprogram.html', {'subprogram':subprogram, 'form': form, 'editing':True})


from django.db.models import F

from reports.pdf_test import header as h
def report(request, subprogram_id):
    subprogram = Subprogram.objects.get(id=subprogram_id)

    #get_gender_category_resume(subprogram)
    #get_gender_social_resume(subprogram)
    #get_social_category_resume(subprogram)

    response = HttpResponse(content_type='application/pdf')

    #pdf_name = "deportistas_por_liga-%s.pdf" % (timezone.now())  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff, topMargin=2.5 * cm,
                            leftMargin=1.5 * cm,
                            rightMargin=1.5 * cm,
                            bottomMargin=2 * cm,
                            pagesize=letter)

    frame = Frame(1.5 * cm, doc.bottomMargin, doc.width, doc.height - doc.bottomMargin,
                  topPadding=0.5 * cm)  # Frame(1.5*cm, 2*cm, doc.width, doc.height-2*cm, id='normal', showboundary)

    header_content = Paragraph("REPORTE DE BENEFICIARIOS POR SUBPROGRAMA", styleH2)
    template = PageTemplate(id='test', frames=frame, onPage=partial(header, content=header_content))
    doc.addPageTemplates([template])

    text = []
    text.append(Paragraph("<br/>", styleH))

    headings = (Paragraph(u'Subprograma: '+subprogram.name+u'<br/>Beneficiarios clasificados por género<br/><br/>', styleH2E),)
    g_data, g_labels = get_gender_resume(subprogram)
    graph = [(BreakdownPieDrawing(8*cm, 8*cm, 2*cm, 0, data=g_data, labels=g_labels),)]
    t = Table([headings] + graph)
    text.append(t)

    headings = (Paragraph(u'<br/><br/>Subprograma: ' + subprogram.name + u'<br/>Beneficiarios clasificados por condición social<br/><br/>', styleH2E),)
    s_data, s_labels = get_social_resume(subprogram)
    graph = [(BreakdownPieDrawing(8 * cm, 8 * cm, 2 * cm, 0, data=s_data, labels=s_labels),)]
    t = Table([headings] + graph)
    text.append(t)

    headings = (Paragraph(u'Subprograma: ' + subprogram.name + u'<br/>Beneficiarios clasificados por rango de edad<br/><br/>', styleH2E),)
    c_data, c_labels = get_category_resume(subprogram)
    graph = [(BreakdownPieDrawing(8 * cm, 8 * cm, 2 * cm, 0, data=c_data, labels=c_labels),)]
    t = Table([headings] + graph)
    text.append(t)

    headings = (Paragraph(u'<br/><br/><br/>Subprograma: ' + subprogram.name + u'<br/>Beneficiarios clasificados por género y condición social<br/><br/>', styleH2E),)
    gs_data, gs_labels, gs_categories = get_gender_social_resume(subprogram)
    graph = [(GroupedBarChart(gs_data, gs_labels, gs_categories, False, False),)]
    t = Table([headings] + graph)
    text.append(t)

    text.append(PageBreak())

    headings = (Paragraph(u'Subprograma: ' + subprogram.name + u'<br/>Beneficiarios clasificados por género y rango de edad<br/><br/>',styleH2E),)
    gc_data, gc_labels, gc_categories = get_gender_category_resume(subprogram)
    graph = [(GroupedBarChart(gc_data, gc_labels, gc_categories, True, False),)]
    t = Table([headings] + graph)
    text.append(t)

    headings = (Paragraph(u'<br/><br/><br/>Subprograma: ' + subprogram.name + u'<br/>Beneficiarios clasificados por condición social y rango de edad<br/><br/>',styleH2E),)
    sc_data, sc_labels, sc_categories = get_social_category_resume(subprogram)
    graph = [(GroupedBarChart(sc_data, sc_labels, sc_categories, True, True),)]
    t = Table([headings] + graph)
    text.append(t)

    text.append(Paragraph("<br/>&nbsp;", styleN))

    doc.build(text)

    response.write(buff.getvalue())
    buff.close()
    return response



def get_gender_resume(subprogram):

    intervs = subprogram.intervention_set.all()

    M = 0
    F = 0

    for interv in intervs:
        sessions = interv.session_set.all()
        for session in sessions:

            categories = session.beneficiarycategory_set.all()

            for cat in categories:
                Mt = cat.beneficiarygroup_set.all().aggregate(
                    Mtotal=Sum('masculine_individuals')
                )['Mtotal']

                Ft = cat.beneficiarygroup_set.all().aggregate(
                    Mtotal=Sum('femenine_individuals')
                )['Mtotal']

                M += Mt
                F += Ft

    return  ([M,F],['Masculino','Femenino'])


def get_social_resume(subprogram):
    intervs = subprogram.intervention_set.all()

    G1 = 0
    G2 = 0
    G3 = 0
    G4 = 0
    G5 = 0

    for interv in intervs:
        sessions = interv.session_set.all()
        for session in sessions:

            categories = session.beneficiarycategory_set.all()

            for cat in categories:
                G1 += cat.beneficiarygroup_set.get(group_name='M').masculine_individuals
                G1 += cat.beneficiarygroup_set.get(group_name='M').femenine_individuals

                G2 += cat.beneficiarygroup_set.get(group_name='I').masculine_individuals
                G2 += cat.beneficiarygroup_set.get(group_name='I').femenine_individuals

                G3 += cat.beneficiarygroup_set.get(group_name='C').masculine_individuals
                G3 += cat.beneficiarygroup_set.get(group_name='C').femenine_individuals

                G4 += cat.beneficiarygroup_set.get(group_name='D').masculine_individuals
                G4 += cat.beneficiarygroup_set.get(group_name='D').femenine_individuals

                G5 += cat.beneficiarygroup_set.get(group_name='A').masculine_individuals
                G5 += cat.beneficiarygroup_set.get(group_name='A').femenine_individuals

    return ([G1, G2, G3, G4, G5],['Mestizos', 'Indígenas', 'Campesinos', 'Pers. con discapacidad', 'Afrodescendientes'])


def get_category_resume(subprogram):
    intervs = subprogram.intervention_set.all()
    data = [0, 0, 0, 0, 0, 0]

    for interv in intervs:
        sessions = interv.session_set.all()
        for session in sessions:

            categories = session.beneficiarycategory_set.all()

            for index, cat in enumerate(categories):
                masc = cat.beneficiarygroup_set.all().aggregate(
                    total=Sum('masculine_individuals')
                )['total']

                masc += cat.beneficiarygroup_set.all().aggregate(
                    total=Sum('femenine_individuals')
                )['total']

                data[index] += masc

    return (data,['0 a 5 Años','6 a 12 Años','13 a 17 Años','18 a 29 Años','30 a 59 Años','Más de 60 Años'])


def get_gender_social_resume(subprogram):
    intervs = subprogram.intervention_set.all()

    G1 = 0
    G2 = 0
    G3 = 0
    G4 = 0
    G5 = 0
    G1f = 0
    G2f = 0
    G3f = 0
    G4f = 0
    G5f = 0

    data = [[0,0,0,0,0],[0,0,0,0,0]]

    for interv in intervs:
        sessions = interv.session_set.all()
        for session in sessions:

            categories = session.beneficiarycategory_set.all()

            for cat in categories:
                G1 += cat.beneficiarygroup_set.get(group_name='M').masculine_individuals
                G1f += cat.beneficiarygroup_set.get(group_name='M').femenine_individuals

                G2 += cat.beneficiarygroup_set.get(group_name='I').masculine_individuals
                G2f += cat.beneficiarygroup_set.get(group_name='I').femenine_individuals

                G3 += cat.beneficiarygroup_set.get(group_name='C').masculine_individuals
                G3f += cat.beneficiarygroup_set.get(group_name='C').femenine_individuals

                G4 += cat.beneficiarygroup_set.get(group_name='D').masculine_individuals
                G4f += cat.beneficiarygroup_set.get(group_name='D').femenine_individuals

                G5 += cat.beneficiarygroup_set.get(group_name='A').masculine_individuals
                G5f += cat.beneficiarygroup_set.get(group_name='A').femenine_individuals

    data = [
        [G1,G2,G3,G4,G5],
        [G1f, G2f, G3f, G4f, G5f],
    ]

    labels = [
        ['Hombres', None] + [str(d) for d in data[0]],
        ['Mujeres', None] + [str(d) for d in data[1]]
    ]
    categories = ['Mest.', 'Indíg.', 'Camp.', 'Pers. con discap.', 'Afrodesc.']

    return (data,labels,categories)


def get_gender_category_resume(subprogram):
    intervs = subprogram.intervention_set.all()
    data = [[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]

    for interv in intervs:
        sessions = interv.session_set.all()
        for session in sessions:

            categories = session.beneficiarycategory_set.all()

            for index, cat in enumerate(categories):
                masc = cat.beneficiarygroup_set.all().aggregate(
                    total=Sum('masculine_individuals')
                )['total']

                data[0][index] += masc

                masc = cat.beneficiarygroup_set.all().aggregate(
                    total=Sum('femenine_individuals')
                )['total']

                data[1][index] += masc
    labels = [
        ['Hombres', None] + [str(d) for d in data[0]],
        ['Mujeres', None] + [str(d) for d in data[1]]
    ]
    categories = ['0 a 5', '6 a 12', '13 a 17', '18 a 29', '30 a 59', '> 60']

    return (data,labels,categories)


def get_social_category_resume(subprogram):
    intervs = subprogram.intervention_set.all()

    G1 = 0
    G2 = 0
    G3 = 0
    G4 = 0
    G5 = 0

    data = [
        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]
    ]

    for interv in intervs:
        sessions = interv.session_set.all()
        for session in sessions:

            categories = session.beneficiarycategory_set.all()

            for index,cat in enumerate(categories):

                G1 = cat.beneficiarygroup_set.get(group_name='M').masculine_individuals
                G1 += cat.beneficiarygroup_set.get(group_name='M').femenine_individuals

                G2 = cat.beneficiarygroup_set.get(group_name='I').masculine_individuals
                G2 += cat.beneficiarygroup_set.get(group_name='I').femenine_individuals

                G3 = cat.beneficiarygroup_set.get(group_name='C').masculine_individuals
                G3 += cat.beneficiarygroup_set.get(group_name='C').femenine_individuals

                G4 = cat.beneficiarygroup_set.get(group_name='D').masculine_individuals
                G4 += cat.beneficiarygroup_set.get(group_name='D').femenine_individuals

                G5 = cat.beneficiarygroup_set.get(group_name='A').masculine_individuals
                G5 += cat.beneficiarygroup_set.get(group_name='A').femenine_individuals

                for i, val in enumerate([G1,G2,G3,G4,G5]):
                    data[i][index] += val

    labels = [
        ['Mest.', None] + [str(d) for d in data[0]],
        ['Indíg.', None] + [str(d) for d in data[1]],
        ['Camp.', None] + [str(d) for d in data[2]],
        ['Pers. con discap.', None] + [str(d) for d in data[3]],
        ['Afrodesc.', None] + [str(d) for d in data[4]],
    ]
    categories = ['0 a 5', '6 a 12', '13 a 17', '18 a 29', '30 a 59', '> 60']

    return data, labels, categories