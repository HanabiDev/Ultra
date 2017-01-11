from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls.base import reverse_lazy

from contractors.models import AppUser
from events.forms import EventForm
from events.models import Event, Rank


def list_events(request):
    events = Event.objects.all()
    return render(request, 'events_list.html', {'events':events})

def create_event(request):
    owner = AppUser.objects.get(user_ptr=request.user.id)
    if request.method == 'GET':
        form = EventForm(initial={'owner':owner})
        return render(request, 'event.html', {'form': form})

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            new_event = form.save()
            return redirect(reverse_lazy('events:view_event', kwargs={'event_id': str(new_event.id)}))

        return render(request, 'event.html', {'form': form})


def view_event(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'event_detail.html', {'event': event})


def update_event(request, event_id):
    event = Event.objects.get(id=event_id)

    if request.method == 'GET':
        form = EventForm(instance=event)
        return render(request, 'event.html', {'form': form})

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)

        if form.is_valid():
            event = form.save()
            return redirect(reverse_lazy('events:view_event', kwargs={'event_id': str(event.id)}))

        return render(request, 'event.html', {'form': form})


def rank_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'GET':
        return render(request, 'rank_event.html', {'event':event})

    if request.method == 'POST':
        for cont in event.contestant_set.all():
            number = request.POST.get(str(cont.id))
            rank = Rank()
            rank.event = event
            rank.contestant = cont
            rank.rank = number
            rank.save()

        return redirect(reverse_lazy('events:list_events'))

def rank_report(request, event_id):
    ranks = Rank.objects.filter(event_id=event_id).order_by('rank')
    return render(request, 'rank_report.html', {'ranks':ranks})
