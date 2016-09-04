from contractors.forms import ContractorForm
from contractors.models import Contractor
from django.shortcuts import render_to_response, render, redirect
from django.template.context import RequestContext
from django.urls.base import reverse_lazy


def list_contractors(request):
    contractors = Contractor.objects.all()
    return render(request, 'contractors_list.html', {'contractors':contractors})


def create_contractor(request):
    if request.method == 'GET':
        form = ContractorForm()
        return render(request, 'contractor.html', {'form': form})

    if request.method == 'POST':
        form = ContractorForm(request.POST, request.FILES)

        if form.is_valid():
            new_contractor = form.save()
            return render(request, 'contractor.html', request.session)

        return render_to_response(request, 'contractor.html', {'form': form})


def view_contractor(request, user_id):
    contractor = Contractor.objects.get(id=user_id)
    return render(request, 'contractor_detail.html', {'contractor': contractor})

def update_contractor(request, user_id):

    contractor = Contractor.objects.get(id=user_id)
    if request.method == 'GET':
        form = ContractorForm(instance=contractor)
        return render(request, 'contractor.html', {'form': form, 'editing': True})

    if request.method == 'POST':
        form = ContractorForm(request.POST, request.FILES, instance=contractor)

        if form.is_valid():
            contractor = form.save()
            return redirect(reverse_lazy('contractors:view', kwargs={'user_id': str(contractor.id)}))

        return render(request, 'contractor.html', {'form': form, 'editing':True})