#encoding: utf-8
from functools import partial
from io import BytesIO

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils.timesince import timesince
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import cm
from reportlab.platypus.doctemplate import SimpleDocTemplate, PageTemplate
from reportlab.platypus.frames import Frame
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.tables import Table, TableStyle

from athletes.forms import AthleteForm, AthleteCardForm, AthleteResultForm, AthleteResultRefForm, AthleteSocialCardForm, AptitudeTestForm, SFPBValorationForm
from athletes.forms import AntropometricValorationForm, PsicologicValorationForm, PhysiologicalTestForm
from athletes.models import Athlete, SportsTab, Result, BiomedicTab, League
from django.urls.base import reverse_lazy

from athletes.templatetags.user_tags import upto
from programs.models import Municipality
from reports.pdf_test import styleH2, header, styleH, styleH2E, styleN, styleH2M, styleNC


def permissions(user):
    return user.is_superuser or user.is_staff


def filter_municipalities(request):
    province_id = request.GET.get('province_id')
    municipalities = Municipality.objects.filter(province=province_id)

    return render(request, 'list.html', {'muns':municipalities})


@login_required(login_url='login')
@user_passes_test(permissions, login_url='login')
def list_athletes(request):
    athletes = Athlete.objects.all()
    return render(request, 'athletes_list.html', {'athletes':athletes})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_athlete(request):

    if request.method == 'GET':
        form = AthleteForm()
        return render(request, 'athlete.html', {'form': form})

    if request.method == 'POST':
        form = AthleteForm(request.POST, request.FILES)

        if form.is_valid():
            new_athlete = form.save()
            return redirect(reverse_lazy('athletes:list_athletes'))
            #return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(new_athlete.id)}))

        return render(request, 'athlete.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def view_athlete(request, user_id):
    athlete = Athlete.objects.get(id=user_id)
    return render(request, 'athlete_detail.html', {'athlete': athlete})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def update_athlete(request, user_id):

    athlete = Athlete.objects.get(id=user_id)
    if request.method == 'GET':
        form = AthleteForm(instance=athlete)
        form.base_fields['photo'].required = False
        form.base_fields['dni_support'].required = False
        return render(request, 'athlete.html', {'athlete':athlete, 'form': form, 'editing':True})

    if request.method == 'POST':
        form = AthleteForm(request.POST, request.FILES, instance=athlete)

        if form.is_valid():
            athlete = form.save()
            return redirect(reverse_lazy('athletes:list_athletes'))
            #return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(athlete.id)}))

        return render(request, 'athlete.html', {'athlete':athlete, 'form': form, 'editing':True})



#=======================================================================  Athlete Card ===================#

@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_athlete_card(request, user_id):
    athlete = Athlete.objects.get(id=user_id)

    if request.method == 'GET':
        form = AthleteCardForm(initial={'athlete':athlete})
        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})

    if request.method == 'POST':
        form = AthleteCardForm(request.POST, request.FILES)

        if form.is_valid():
            new_card = form.save()
            return redirect(reverse_lazy('athletes:view_athlete', kwargs={'user_id': str(athlete.id)}))
            #return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(new_athlete.id)}))

        return render(request, 'athlete.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def edit_athlete_card(request, user_id):
    athlete = Athlete.objects.get(id=user_id)
    card = SportsTab.objects.get(athlete__id=user_id)

    if request.method == 'GET':
        form = AthleteCardForm(instance=card, initial={'athlete':athlete})
        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})

    if request.method == 'POST':
        form = AthleteCardForm(request.POST, request.FILES, instance=card)

        if form.is_valid():
            new_card = form.save()
            return redirect(reverse_lazy('athletes:view_athlete', kwargs={'user_id': str(athlete.id)}))
            #return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(new_athlete.id)}))

        return render(request, 'athlete.html', {'form': form})


#=======================================================================  Athlete Results ===================#

@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_athlete_result(request, user_id):
    athlete = Athlete.objects.get(id=user_id)

    if request.method == 'GET':
        form = AthleteResultForm(initial={'athlete':athlete})
        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})

    if request.method == 'POST':
        form = AthleteResultForm(request.POST, request.FILES)

        if form.is_valid():
            new_card = form.save()
            return redirect(reverse_lazy('athletes:view_athlete', kwargs={'user_id': str(athlete.id)}))
            #return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(new_athlete.id)}))

        return render(request, 'result.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def edit_athlete_result(request, user_id, result_id):
    athlete = Athlete.objects.get(id=user_id)
    result = Result.objects.get(id=result_id)

    if request.method == 'GET':
        form = AthleteResultForm(instance=result, initial={'athlete':athlete})
        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete})

    if request.method == 'POST':
        form = AthleteCardForm(request.POST, request.FILES, instance=card)

        if form.is_valid():
            new_card = form.save()
            return redirect(reverse_lazy('athletes:view_athlete', kwargs={'user_id': str(athlete.id)}))
            #return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(new_athlete.id)}))

        return render(request, 'athlete.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_athlete_result_ref(request, user_id, result_id):
    athlete = Athlete.objects.get(id=user_id)
    result = Result.objects.get(id=result_id)

    if request.method == 'GET':
        form = AthleteResultRefForm(initial={'result':result})
        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})

    if request.method == 'POST':
        form = AthleteResultRefForm(request.POST, request.FILES)

        if form.is_valid():
            new_card = form.save()
            return redirect(reverse_lazy('athletes:view_athlete', kwargs={'user_id': str(athlete.id)}))
            #return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(new_athlete.id)}))

        return render(request, 'result.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_athlete_socialcard(request, user_id):
    athlete = Athlete.objects.get(id=user_id)

    if request.method == 'GET':
        form = AthleteSocialCardForm(initial={'athlete':athlete})
        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})

    if request.method == 'POST':
        form = AthleteSocialCardForm(request.POST, request.FILES)

        if form.is_valid():
            new_card = form.save()
            return redirect(reverse_lazy('athletes:view_athlete', kwargs={'user_id': str(athlete.id)}))
            #return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(new_athlete.id)}))

        return render(request, 'athlete.html', {'form': form})


#=======================================================================  Athlete Social Card ================#


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def edit_athlete_socialcard(request, user_id):
    athlete = Athlete.objects.get(id=user_id)
    card = SportsTab.objects.get(athlete__id=user_id)

    if request.method == 'GET':
        form = AthleteCardForm(instance=card, initial={'athlete':athlete})
        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})

    if request.method == 'POST':
        form = AthleteCardForm(request.POST, request.FILES, instance=card)

        if form.is_valid():
            new_card = form.save()
            return redirect(reverse_lazy('athletes:view_athlete', kwargs={'user_id': str(athlete.id)}))
            #return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(new_athlete.id)}))

        return render(request, 'athlete.html', {'form': form})


#==================================================================  Athlete Biomedic Card ===================#

def create_biomedic_card(request, user_id):
    athlete = Athlete.objects.get(id=user_id)

    if request.method == 'GET':
        biomedic_card = BiomedicTab(athlete=athlete)
        biomedic_card.save()
        form = AptitudeTestForm(initial={'tab':biomedic_card})
        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})

    if request.method == 'POST':
        form = AptitudeTestForm(request.POST)

        if form.is_valid():
            new_card = form.save()
            return redirect(reverse_lazy('athletes:SFPBValoration', kwargs={'tab_id': str(new_card.tab.id), 'user_id':str(athlete.id)}))

        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})


def create_SFPB_valoration(request, user_id, tab_id):
    tab = BiomedicTab.objects.get(id=tab_id)
    athlete = Athlete.objects.get(id=user_id)

    if request.method == 'GET':
        form = SFPBValorationForm(initial={'tab':tab})
        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})

    if request.method == 'POST':
        form = SFPBValorationForm(request.POST)

        if form.is_valid():
            new_card = form.save()
            return redirect(reverse_lazy('athletes:antropo', kwargs={'tab_id': str(new_card.tab.id), 'user_id':str(athlete.id)}))

        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})


def create_antropometric_valoration(request, user_id, tab_id):
    tab = BiomedicTab.objects.get(id=tab_id)
    athlete = Athlete.objects.get(id=user_id)

    if request.method == 'GET':
        form = AntropometricValorationForm(initial={'tab':tab})
        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})

    if request.method == 'POST':
        form = AntropometricValorationForm(request.POST)

        if form.is_valid():
            new_card = form.save()
            return redirect(reverse_lazy('athletes:psico', kwargs={'tab_id': str(new_card.tab.id), 'user_id':str(athlete.id)}))

        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})



def create_psicologic_valoration(request, user_id, tab_id):
    tab = BiomedicTab.objects.get(id=tab_id)
    athlete = Athlete.objects.get(id=user_id)

    if request.method == 'GET':
        form = PsicologicValorationForm(initial={'tab':tab})
        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})

    if request.method == 'POST':
        form = PsicologicValorationForm(request.POST)

        if form.is_valid():
            new_card = form.save()
            return redirect(reverse_lazy('athletes:physio', kwargs={'tab_id': str(new_card.tab.id), 'user_id':str(athlete.id)}))

        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})



def create_physiological_valoration(request, user_id, tab_id):
    tab = BiomedicTab.objects.get(id=tab_id)
    athlete = Athlete.objects.get(id=user_id)

    if request.method == 'GET':
        form = PhysiologicalTestForm(initial={'tab':tab})
        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})

    if request.method == 'POST':
        form = PhysiologicalTestForm(request.POST)

        if form.is_valid():
            new_card = form.save()
            return redirect(reverse_lazy('athletes:view_athlete', kwargs={'user_id':str(athlete.id)}))

        return render(request, 'athlete_card.html', {'form': form, 'athlete':athlete, 'sports':True})

from django.utils import timezone
def report_athletes(request):
    if request.method == 'GET':
        leagues = League.objects.all();
        return render(request, 'report_filter.html', {'leagues': leagues})

    if request.method == 'POST':
        response = HttpResponse(content_type='application/pdf')

        pdf_name = "deportistas_por_liga-%s.pdf" % (timezone.now())  # llamado clientes
        # la linea 26 es por si deseas descargar el pdf a tu computadora
        # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
        buff = BytesIO()
        doc = SimpleDocTemplate(buff, topMargin=2.5 * cm,
                                leftMargin=1.5 * cm,
                                rightMargin=1.5 * cm,
                                bottomMargin=2 * cm,
                                pagesize=landscape(letter))

        frame = Frame(1.5 * cm, doc.bottomMargin, doc.width, doc.height - doc.bottomMargin,
                      topPadding=0.5 * cm)  # Frame(1.5*cm, 2*cm, doc.width, doc.height-2*cm, id='normal', showboundary)

        header_content = Paragraph("REPORTE DE DEPORTISTAS POR LIGA", styleH2)
        template = PageTemplate(id='test', frames=frame, onPage=partial(header, content=header_content))
        doc.addPageTemplates([template])

        text = []
        text.append(Paragraph("<br/>", styleH))

        id = request.POST.get('league')

        leagues = [League.objects.get(id=int(id)).order_by('name'),] if id != '0' else  League.objects.all()

        for league in leagues:
            if league.sportstab_set.all().count() >0:
                text.append(Paragraph(league.name, styleH2M))
                headings = ('#','Nombre', 'Documento', 'Edad', 'Deporte', 'Club')
                all_athletes = [(
                    i+1,
                    Paragraph(t.athlete.__unicode__(), styleN),
                    Paragraph(t.athlete.document_number, styleNC),
                    Paragraph(upto(timesince(t.athlete.birth_date),','), styleNC),
                    Paragraph(t.athlete.sportstab_set.first().sport.__unicode__(), styleNC),
                    Paragraph(t.athlete.sportstab_set.first().club.__unicode__(), styleNC)
                ) for i, t in enumerate(league.sportstab_set.all().order_by('athlete__first_name'))]

                t = Table([headings] + all_athletes, colWidths=[1*cm]+[9*cm,3*cm, 2*cm, 5*cm, 5*cm])
                t.setStyle(TableStyle([('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                                       ('ALIGN', (2, 1), (-1, -1), 'CENTER'),
                                       ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                       ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                                       ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor("#333333")),
                                       ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                       ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.transparent),
                                       ('INNERGRID', (0, 1), (-1, -1), 0.5, colors.HexColor("#27ae60")),
                                       ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#27ae60")),
                                       ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#27ae60")),
                                       ]))
                text.append(t)
                text.append(Paragraph("<br/>&nbsp;", styleN))


        doc.build(text)

        response.write(buff.getvalue())
        buff.close()
        return response