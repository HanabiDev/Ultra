from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from athletes.forms import AthleteForm, AthleteCardForm, AthleteResultForm, AthleteResultRefForm, AthleteSocialCardForm
from athletes.models import Athlete, SportsTab, Result
from django.urls.base import reverse_lazy
from programs.models import Municipality

def permissions(user):
    return user.is_superuser or user.is_staff


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
        return render(request, 'athlete.html', {'athlete':athlete, 'form': form, 'editing':True})

    if request.method == 'POST':
        form = AthleteForm(request.POST, request.FILES, instance=athlete)

        if form.is_valid():
            athlete = form.save()
            return redirect(reverse_lazy('athletes:list_athletes'))
            #return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(athlete.id)}))

        return render(request, 'athlete.html', {'athlete':athlete, 'form': form, 'editing':True})


def filter_municipalities(request):
    province_id = request.GET.get('province_id')
    municipalities = Municipality.objects.filter(province=province_id)

    return render(request, 'list.html', {'muns':municipalities})
