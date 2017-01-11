#encoding: utf-8
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from django.urls.base import reverse_lazy

from events.forms import EventForm, ContestantForm
from events.models import Event, Contestant
from polls.models import Poll, Option


def home(request):
    polls = Poll.objects.filter(closed=False).order_by('-creation_date')[:5]
    events = Event.objects.filter(open=True)[:5]
    return render(request, 'site/base/base.html', {'polls':polls, 'events':events})

def list_polls(request):
    polls = Poll.objects.filter(closed=False).order_by('-creation_date')
    return render(request, 'poll_index.html', {'polls': polls})

from django.contrib import messages
def answer_poll(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method == 'GET':
        return render(request, 'fill_poll.html', {'poll':poll})

    if request.method == 'POST':
        poll.hits = poll.hits+1
        poll.save()
        for question in poll.question_set.all():
            option_id = request.POST.get('q_'+str(question.id))
            option = Option.objects.get(id=option_id)
            option.hits = option.hits+1
            option.save()


        messages.success(request, 'Sus respuestas han sido enviadas. Gracias por su colaboración!')
        return redirect(reverse_lazy('site:home'))

def list_events(request):
    events = Event.objects.filter(open=True)
    return render(request, 'events.html', {'events':events})

def event_suscribe(request, event_id):

    event = Event.objects.get(id=event_id)
    cid = 1
    try:
        last = event.contestant_set.all().order_by('-id')[0]
        cid = last.cid+1
    except:
        pass


    if request.method == 'GET':

        form = ContestantForm(initial={'event':event, 'cid':cid})
        return render(request, 'suscribe.html', {'form':form, 'event':event})

    if request.method == 'POST':
        form = ContestantForm(request.POST, request.FILES, initial={'event':event, 'cid':cid})

        if form.is_valid():
            contestant = form.save()
            send_inscription_mail(event, contestant)
            messages.success(request, 'Se ha registrado su inscripción. Revise su correo para más detalles')
            return redirect(reverse_lazy('site:home'))
        return render(request, 'suscribe.html', {'form': form, 'event': event})



def send_inscription_mail(event, contestant):
    send_mail(
        subject=u'Confirmación de inscripción',
        message=u"""Confirmación de inscripción.
                   Se ha realizado correctamente su inscripción en el evento """+event.name+u""", con los siguientes datos:
                   Nombre completo:"""+contestant.first_name+u' '+contestant.last_name+u"""
                   Documento: """+contestant.dni+u"""
                   Teléfono: """+contestant.phone+u"""
                   Correo: """+contestant.email+u"""
                   Ciudad: """+contestant.city+u"""
                   Número asignado: """+str(contestant.cid)+u"""
                   Recuerde mantener este correo en caso de que se le requiera.""",
        html_message=u"""<p><b>Señor </b><br>"""+contestant.first_name+u' '+contestant.last_name+u"""</b></p>
                    <p>Se ha registrado su inscripción al evento \""""+event.name+u"""\".<p>
                    <p>
                        A continuación se resume la información registrada.<br/>
                        <b>Nombre completo: </b>"""+contestant.first_name+u' '+contestant.last_name+u"""<br/>
                        <b>Documento: </b>"""+contestant.dni+u"""<br/>
                        <b>Teléfono: </b>"""+contestant.phone+u"""<br/>
                        <b>Correo: </b>"""+contestant.email+u"""<br/>
                        <b>Ciudad: </b>"""+contestant.city+u"""<br/>
                        <b>Número asignado: </b>"""+str(contestant.cid)+u"""<br/>
                    </p> Recuerde mantener una copia de este correo por si le es solicitada.""",
        from_email='Ultra <ultra@indeportes.gov.co>',
        recipient_list=[contestant.email],
        fail_silently=False
    )

