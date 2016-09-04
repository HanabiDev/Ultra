from contractors.forms import ContractorForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def create_contractor(request):
    if request.method == 'GET':
        form = ContractorForm()
        return render_to_response('contractor.html', {'form': form})

    if request.method == 'POST':
        form = ContractorForm(request.POST, request.FILES)

        if form.is_valid():
            new_contractor = form.save()
            return render_to_response('contractor.html')

        return render_to_response('contractor.html', {'form': form})