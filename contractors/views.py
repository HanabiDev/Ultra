from athletes.views import permissions
from contractors.forms import ContractorForm, EditContractorForm, PasswordForm, FormationItemForm, AchievementForm, \
    InterventionForm
from contractors.models import Contractor, FormationItem, SportsAchievements, Intervention, TimeSchedule
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render_to_response, render, redirect
from django.template.context import RequestContext
from django.urls.base import reverse_lazy

@login_required(login_url='login')
@user_passes_test(permissions, login_url='login')
def list_contractors(request):
    contractors = Contractor.objects.all()
    return render(request, 'contractors_list.html', {'contractors':contractors})

@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_contractor(request):
    if request.method == 'GET':
        form = ContractorForm()
        return render(request, 'contractor.html', {'form': form})

    if request.method == 'POST':
        form = ContractorForm(request.POST, request.FILES)

        if form.is_valid():
            new_contractor = form.save()
            return redirect(reverse_lazy('contractors:view_contractor', kwargs={'user_id': str(new_contractor.id)}))

        return render(request, 'contractor.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def view_contractor(request, user_id):
    contractor = Contractor.objects.get(id=user_id)
    return render(request, 'contractor_detail.html', {'contractor': contractor})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def update_contractor(request, user_id):

    pass_change = False
    if request.session.get('pass_changed'):
        pass_change = True
        del request.session['pass_changed']

    contractor = Contractor.objects.get(id=user_id)
    if request.method == 'GET':
        form = EditContractorForm(instance=contractor)
        return render(request, 'contractor.html', {'contractor':contractor, 'pass':pass_change, 'form': form, 'editing': True})

    if request.method == 'POST':
        form = EditContractorForm(request.POST, request.FILES, instance=contractor)

        if form.is_valid():
            contractor = form.save()
            return redirect(reverse_lazy('contractors:view_contractor', kwargs={'user_id': str(contractor.id)}))

        return render(request, 'contractor.html', {'contractor':contractor, 'form': form, 'pass':pass_change, 'editing':True})



@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def add_formation(request, user_id):

    contractor = Contractor.objects.get(id=user_id)
    if request.method == 'GET':
        form = FormationItemForm(initial={'trainer':contractor})
        return render(request, 'formation.html', {'contractor':contractor, 'form': form, 'formation':True})

    if request.method == 'POST':
        form = FormationItemForm(request.POST, request.FILES)

        if form.is_valid():
            formation_item = form.save()
            return redirect(reverse_lazy('contractors:view_contractor', kwargs={'user_id': str(contractor.id)}))

        return render(request, 'formation.html', {'contractor':contractor, 'form': form, 'formation':True})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def edit_formation(request, user_id, formation_id):

    contractor = Contractor.objects.get(id=user_id)
    formation = FormationItem.objects.get(id=formation_id)

    if request.method == 'GET':
        form = FormationItemForm(instance=formation, initial={'trainer':contractor})

        print form
        return render(request, 'formation.html', {'contractor':contractor, 'form': form, 'formation':True, 'editing':True})

    if request.method == 'POST':
        form = FormationItemForm(request.POST, request.FILES, instance=formation)

        if form.is_valid():
            formation_item = form.save()
            return redirect(reverse_lazy('contractors:view_contractor', kwargs={'user_id': str(contractor.id)}))

        return render(request, 'formation.html', {'contractor':contractor, 'form': form, 'formation':True, 'editing':True})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def delete_formation(request, user_id, formation_id):
    formation = FormationItem.objects.get(id=formation_id, trainer__id=user_id)
    formation.delete()
    return redirect(reverse_lazy('contractors:view_contractor', kwargs={'user_id': str(user_id)}))


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def add_achievement(request, user_id):

    contractor = Contractor.objects.get(id=user_id)
    if request.method == 'GET':
        form = AchievementForm(initial={'trainer':contractor})
        return render(request, 'formation.html', {'contractor':contractor, 'form': form})

    if request.method == 'POST':
        form = AchievementForm(request.POST, request.FILES)

        if form.is_valid():
            achievement = form.save()
            return redirect(reverse_lazy('contractors:view_contractor', kwargs={'user_id': str(contractor.id)}))

        return render(request, 'formation.html', {'contractor':contractor, 'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def edit_achievement(request, user_id, achievement_id):

    contractor = Contractor.objects.get(id=user_id)
    achievement = SportsAchievements.objects.get(id=achievement_id)

    if request.method == 'GET':
        form = FormationItemForm(instance=achievement, initial={'trainer':contractor})
        return render(request, 'formation.html', {'contractor':contractor, 'form': form, 'formation':True, 'editing':True})

    if request.method == 'POST':
        form = FormationItemForm(request.POST, request.FILES, instance=achievement)

        if form.is_valid():
            achievement = form.save()
            return redirect(reverse_lazy('contractors:view_contractor', kwargs={'user_id': str(contractor.id)}))

        return render(request, 'formation.html', {'contractor':contractor, 'form': form, 'formation':True, 'editing':True})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def delete_achievement(request, user_id, achievement_id):
    achievement = SportsAchievements.objects.get(id=achievement_id, trainer__id=user_id)
    achievement.delete()
    return redirect(reverse_lazy('contractors:view_contractor', kwargs={'user_id': str(user_id)}))

@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def update_password(request, user_id):
    user = Contractor.objects.get(id=user_id)

    if request.method == 'GET':
        form = PasswordForm(user, None)
        return render(request, 'update_password.html', {'form':form, 'editing':True, 'contractor':user})

    if request.method == 'POST':
        form = PasswordForm(user,request.POST)
        if form.is_valid():
            form.save()
            request.session['pass_changed']=True
            return redirect('contractors:edit_contractor', user_id=user_id)

        return render(request, 'update_password.html', {'form':form, 'editing':True, 'contractor':user})



@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def toggle_lock(request, user_id):
    contractor = Contractor.objects.get(id=user_id)
    contractor.is_active = not contractor.is_active
    contractor.save()
    return redirect(reverse_lazy('contractors:view_contractor', kwargs={'user_id': str(contractor.id)}))



@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def add_interv(request, user_id):
    contractor = Contractor.objects.get(id=user_id)

    if request.method == 'GET':
        form = InterventionForm(initial={'contractor':contractor})
        return render(request, 'contractor_interv.html', {'form': form, 'contractor': contractor})

    if request.method == 'POST':
        form = InterventionForm(request.POST)
        if form.is_valid():
            inter = form.save()
            sched_data = request.POST.get('schedule')
            sched_dict = json.loads(sched_data)

            for index, day in enumerate(sched_dict):
                if day["isActive"]:
                    sched = TimeSchedule(
                        day=TimeSchedule.WEEK_DAYS[index][0],
                        startTime=day["timeFrom"],
                        endTime=day["timeTill"],
                        intervention=inter
                    )

                    sched.save()
            return redirect('contractors:view_contractor', user_id=user_id)

        return render(request, 'contractor_interv.html', {'form': form, 'contractor': contractor})

import json
@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def edit_interv(request, user_id, interv_id):
    contractor = Contractor.objects.get(id=user_id)
    interv = Intervention.objects.get(id=interv_id)

    if request.method == 'GET':
        form = InterventionForm(initial={'contractor':contractor}, instance=interv)

        days = {'Lu':0, 'Ma':1, 'Mi':2, 'Ju':3, 'Vi':4, 'Sa':5, 'Do':6}
        data = []

        for d in days:
            data.append({
                'isActive': False,
                'timeFrom': None,
                'timeTill': None
            })
        for i in interv.timeschedule_set.all():
            data[days[i.day]]["isActive"] = True
            data[days[i.day]]["timeFrom"] = str(i.startTime)
            data[days[i.day]]["timeTill"] = str(i.endTime)

        print json.dumps(data)

        return render(request, 'contractor_interv.html', {'form': form, 'editing': True, 'data':json.dumps(data), 'contractor': contractor})

    if request.method == 'POST':

        interv.timeschedule_set.all().delete()

        form = InterventionForm(request.POST, instance=interv)
        if form.is_valid():
            inter = form.save()
            sched_data = request.POST.get('schedule')
            sched_dict = json.loads(sched_data)

            for index, day in enumerate(sched_dict):
                if day["isActive"]:
                    sched = TimeSchedule(
                        day=TimeSchedule.WEEK_DAYS[index][0],
                        startTime=day["timeFrom"],
                        endTime=day["timeTill"],
                        intervention=inter
                    )

                    sched.save()
            return redirect('contractors:view_contractor', user_id=user_id)

        return render(request, 'contractor_interv.html', {'form': form, 'editing': True, 'contractor': contractor})