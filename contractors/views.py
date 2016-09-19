from athletes.views import permissions
from contractors.forms import ContractorForm
from contractors.models import Contractor
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

    contractor = Contractor.objects.get(id=user_id)
    if request.method == 'GET':
        form = ContractorForm(instance=contractor)
        return render(request, 'contractor.html', {'contractor':contractor, 'form': form, 'editing': True})

    if request.method == 'POST':
        form = ContractorForm(request.POST, request.FILES, instance=contractor)

        if form.is_valid():
            contractor = form.save()
            return redirect(reverse_lazy('contractors:view_contractor', kwargs={'user_id': str(contractor.id)}))

        return render(request, 'contractor.html', {'contractor':contractor, 'form': form, 'editing':True})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def toggle_lock(request, user_id):
    contractor = Contractor.objects.get(id=user_id)
    contractor.is_active = not contractor.is_active
    contractor.save()
    return redirect(reverse_lazy('contractors:view_contractor', kwargs={'user_id': str(contractor.id)}))