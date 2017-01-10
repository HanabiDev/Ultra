#encoding: utf-8
from django.shortcuts import render, redirect

# Create your views here.
from django.urls.base import reverse_lazy

from events.models import Event
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