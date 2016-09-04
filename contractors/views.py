from django.shortcuts import render_to_response
from django.template.context import RequestContext


def create_contractor(request):
    return render_to_response('contractor.html', {})