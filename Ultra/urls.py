"""Ultra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import app_auth.views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.http import HttpResponse


def toggle_sidebar(request):
    #del request.session['sidebar_off']
    request.session['sidebar_off']= not request.session.get('sidebar_off')

    return HttpResponse("OK")


urlpatterns = [
    url(r'^$', app_auth.views.home, name='home'),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^toggle_sidebar/', toggle_sidebar),
    url(r'^auth/', include('app_auth.urls', 'auth')),
    url(r'^auth/login/$', app_auth.views.app_login, name='login'),
    url(r'^auth/logout/$', app_auth.views.app_logout, name='logout'),
    url(r'^programas/', include('programs.urls.program_urls', 'programs')),
    url(r'^subprogramas/', include('programs.urls.subprogram_urls', 'subprograms')),
    url(r'^contratistas/', include('contractors.urls', 'contractors')),
    url(r'^deportistas/', include('athletes.urls', 'athletes'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
