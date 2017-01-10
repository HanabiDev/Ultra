#encoding: utf-8
from functools import partial
from io import BytesIO

from django.http.response import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.platypus.doctemplate import SimpleDocTemplate, PageTemplate
from reportlab.platypus.frames import Frame
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.tables import Table

from athletes.views import permissions
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy

from contractors.models import Intervention
from polls.forms import PollForm, QuestionForm, OptionForm
from polls.models import Poll, Question, Option
from reports.pdf_test import styleH2, header, styleH, styleN, styleH2E
from reports.plot_types import BreakdownPieDrawing


@login_required(login_url='login')
@user_passes_test(permissions, login_url='login')
def list_polls(request):
    polls = Poll.objects.all()
    return render(request, 'polls_list.html', {'polls':polls})

@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_poll(request):
    if request.method == 'GET':
        form = PollForm()
        return render(request, 'poll.html', {'form': form})

    if request.method == 'POST':
        form = PollForm(request.POST, request.FILES)

        if form.is_valid():
            new_poll = form.save()
            return redirect(reverse_lazy('polls:view_poll', kwargs={'poll_id': str(new_poll.id)}))

        return render(request, 'poll.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def view_poll(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    return render(request, 'poll_detail.html', {'poll': poll})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def update_poll(request, poll_id):

    poll = Poll.objects.get(id=poll_id)
    if request.method == 'GET':
        form = PollForm(instance=poll)
        return render(request, 'poll.html', {'poll':poll, 'form': form, 'editing': True})

    if request.method == 'POST':
        form = PollForm(request.POST, request.FILES, instance=poll)

        if form.is_valid():
            poll = form.save()
            return redirect(reverse_lazy('polls:view_poll', kwargs={'poll_id': str(poll.id)}))

        return render(request, 'poll.html', {'poll':poll, 'form': form, 'editing':True})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def toggle_lock(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    poll.closed = not poll.closed
    poll.save()
    return redirect(reverse_lazy('polls:list_polls'))

def report_poll(request, poll_id):
    poll = Poll.objects.get(id=poll_id)

    response = HttpResponse(content_type='application/pdf')

    # pdf_name = "deportistas_por_liga-%s.pdf" % (timezone.now())  # llamado clientes
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

    header_content = Paragraph("RESULTADOS DE ENCUESTA", styleH2)
    template = PageTemplate(id='test', frames=frame, onPage=partial(header, content=header_content))
    doc.addPageTemplates([template])

    text = []
    text.append(Paragraph("<p><b>Encuesta:</b> " + u''+poll.title+"</p>", styleN))
    text.append(Paragraph("<p><b>Fecha:</b> " + str(poll.creation_date)+"</p>", styleN))
    text.append(Paragraph("<p><b>Número de envíos:</b> " + str(poll.hits) + "</p>", styleN))
    text.append(Paragraph("<br/>&nbsp;", styleN))

    for index, question in enumerate(poll.question_set.all()):
        headings = (
        Paragraph(u'Pregunta '+str(index+1)+u': '+question.statement, styleH2E),)
        q_data = list(question.option_set.all().values_list('hits', flat=True))
        q_data = [(data*100)/sum(q_data) for data in q_data]
        q_labels = list(question.option_set.all().values_list('text', flat=True))
        graph = [(BreakdownPieDrawing(8 * cm, 8 * cm, 2 * cm, 0, data=q_data, labels=q_labels, percents=True),)]
        t = Table([headings] + graph)
        text.append(t)
        text.append(Paragraph("<br/>&nbsp;", styleN))






    """
    headings = (Paragraph(
        u'<br/><br/>Subprograma: ' + subprogram.name + u'<br/>Beneficiarios clasificados por condición social<br/><br/>',
        styleH2E),)
    s_data, s_labels = get_social_resume(subprogram)
    graph = [(BreakdownPieDrawing(8 * cm, 8 * cm, 2 * cm, 0, data=s_data, labels=s_labels),)]
    t = Table([headings] + graph)
    text.append(t)

    headings = (
    Paragraph(u'Subprograma: ' + subprogram.name + u'<br/>Beneficiarios clasificados por rango de edad<br/><br/>',
              styleH2E),)
    c_data, c_labels = get_category_resume(subprogram)
    graph = [(BreakdownPieDrawing(8 * cm, 8 * cm, 2 * cm, 0, data=c_data, labels=c_labels),)]
    t = Table([headings] + graph)
    text.append(t)

    headings = (Paragraph(
        u'<br/><br/><br/>Subprograma: ' + subprogram.name + u'<br/>Beneficiarios clasificados por género y condición social<br/><br/>',
        styleH2E),)
    gs_data, gs_labels, gs_categories = get_gender_social_resume(subprogram)
    graph = [(GroupedBarChart(gs_data, gs_labels, gs_categories, False, False),)]
    t = Table([headings] + graph)
    text.append(t)

    text.append(PageBreak())

    headings = (Paragraph(
        u'Subprograma: ' + subprogram.name + u'<br/>Beneficiarios clasificados por género y rango de edad<br/><br/>',
        styleH2E),)
    gc_data, gc_labels, gc_categories = get_gender_category_resume(subprogram)
    graph = [(GroupedBarChart(gc_data, gc_labels, gc_categories, True, False),)]
    t = Table([headings] + graph)
    text.append(t)

    headings = (Paragraph(
        u'<br/><br/><br/>Subprograma: ' + subprogram.name + u'<br/>Beneficiarios clasificados por condición social y rango de edad<br/><br/>',
        styleH2E),)
    sc_data, sc_labels, sc_categories = get_social_category_resume(subprogram)
    graph = [(GroupedBarChart(sc_data, sc_labels, sc_categories, True, True),)]
    t = Table([headings] + graph)
    text.append(t)


    """

    doc.build(text)

    response.write(buff.getvalue())
    buff.close()
    return response


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_question(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method == 'GET':
        form = QuestionForm(initial={'poll':poll})
        return render(request, 'question.html', {'form': form})

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)

        if form.is_valid():
            new_question = form.save()
            return redirect(reverse_lazy('polls:view_question',
                                         kwargs={'poll_id': str(poll.id), 'question_id': str(new_question.id)}))

        return render(request, 'question.html', {'form': form})



@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def view_question(request, poll_id, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'question_detail.html', {'question': question})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def update_question(request, poll_id, question_id):
    poll = Poll.objects.get(id=poll_id)
    question = Question.objects.get(id=question_id)
    if request.method == 'GET':
        form = QuestionForm(instance=question, initial={'poll':poll})
        return render(request, 'question.html', {'question':question, 'form': form, 'editing': True})

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=question)

        if form.is_valid():
            question = form.save()
            return redirect(reverse_lazy('polls:view_poll', kwargs={'poll_id': str(poll.id)}))

        return render(request, 'question.html', {'poll':poll, 'form': form, 'editing':True})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_option(request, poll_id, question_id):
    poll = Poll.objects.get(id=poll_id)
    question = Question.objects.get(id=question_id)

    if request.method == 'GET':
        form = OptionForm(initial={'question':question})
        return render(request, 'option.html', {'form': form})

    if request.method == 'POST':
        form = OptionForm(request.POST, request.FILES)

        if form.is_valid():
            new_option = form.save()
            return redirect(reverse_lazy('polls:view_question',
                                         kwargs={'poll_id': str(poll.id), 'question_id': str(question.id)}))

        return render(request, 'option.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def update_option(request, poll_id, question_id, option_id):
    poll = Poll.objects.get(id=poll_id)
    question = Question.objects.get(id=question_id)
    option = Option.objects.get(id=option_id)

    if request.method == 'GET':
        form = OptionForm(instance=option, initial={'question':question})
        return render(request, 'option.html', {'question':question, 'form': form, 'editing': True})

    if request.method == 'POST':
        form = OptionForm(request.POST, request.FILES, instance=option)

        if form.is_valid():
            option = form.save()
            return redirect(reverse_lazy('polls:view_question',
                                         kwargs={'poll_id': str(poll.id), 'question_id': str(question.id)}))

        return render(request, 'option.html', {'poll':poll, 'form': form, 'editing':True})