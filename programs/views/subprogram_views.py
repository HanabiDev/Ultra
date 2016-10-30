#encoding: utf-8
from functools import partial
from io import BytesIO

from django.http.response import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus.doctemplate import SimpleDocTemplate, BaseDocTemplate, PageTemplate
from reportlab.platypus.frames import Frame
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.tables import Table, TableStyle

from athletes.views import permissions
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy

from contractors.models import AppUser
from programs.models import Program, Subprogram
from programs.forms import SubprogramForm
from reports.pdf_test import styleH2, styleN, styleH2E, styleH


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


from reports.pdf_test import header as h
def report(request, subprogram_id):
    subprogram = Subprogram.objects.get(id=subprogram_id)

    response = HttpResponse(content_type='application/pdf')
    pdf_name = "beneficiarios.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff, topMargin=2.5*cm,
                                  leftMargin=1.5*cm,
                                  rightMargin=1.5*cm,
                                  bottomMargin=1.5*cm,
                                  pagesize=letter)

    frame = Frame(1.5 * cm, doc.bottomMargin, doc.width, doc.height - doc.bottomMargin,
                  topPadding=0.5 * cm)  # Frame(1.5*cm, 2*cm, doc.width, doc.height-2*cm, id='normal', showboundary)

    header_content = Paragraph("REPORTE DE BENEFICIARIOS POR SUBPROGRAMA", styleH2)
    template = PageTemplate(id='test', frames=frame, onPage=partial(h, content=header_content))
    doc.addPageTemplates([template])

    text = []
    text.append(Paragraph("<br/>", styleH))
    text.append(Paragraph("Beneficiarios del Subrograma: "+subprogram.name+"",styleH2E))
    text.append(Paragraph("(Clasificación por rango de edad)", styleH2E))

    text.append(Paragraph("<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>"
                          "<br/><br/><br/><br/>Beneficiarios del Subrograma: " + subprogram.name + "", styleH2E))
    text.append(Paragraph("(Clasificación por condición social)", styleH2E))

    doc.build(text)

    response.write(buff.getvalue())
    buff.close()
    return response