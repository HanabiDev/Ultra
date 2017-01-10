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
    url(r'^admin/$', app_auth.views.admin_home, name='admin_home'),
    url(r'^admin/auth/', include('app_auth.urls', 'auth')),
    url(r'^admin/auth/login/$', app_auth.views.app_login, name='login'),
    url(r'^admin/auth/logout/$', app_auth.views.app_logout, name='logout'),
    url(r'^admin/programas/', include('programs.urls.program_urls', 'programs')),
    url(r'^admin/subprogramas/', include('programs.urls.subprogram_urls', 'subprograms')),
    url(r'^admin/proyectos/', include('programs.urls.project_urls', 'projects')),
    url(r'^admin/contratistas/', include('contractors.urls', 'contractors')),
    url(r'^admin/deportistas/', include('athletes.urls', 'athletes')),
    url(r'^admin/encuestas/', include('polls.urls', 'polls')),
    url(r'^eventos/', include('events.urls', 'events')),
    url(r'^sitio/', include('main_site.urls', 'site')),


    url(r'^contratista/$', app_auth.views.contractor_home, name='contractor_home'),
    url(r'^contratista/reportar-evento/$', app_auth.views.activity_report, name='activity_report'),
    url(r'^contratista/perfil/$', app_auth.views.contractor_profile, name='contractor_profile'),
    url(r'^contratista/perfil/actualizar/$', app_auth.views.edit_contractor_profile, name='contractor_profile_update'),
    url(r'^contratista/perfil/cambiar-clave/$', app_auth.views.set_contractor_pass, name='contractor_password'),

    url(r'^contratista/perfil/agregar-formacion/$', app_auth.views.add_formation, name='contractor_formation'),
    url(r'^contratista/perfil/editar-formacion/(?P<formation_id>\d+)$', app_auth.views.edit_formation, name='edit_contractor_formation'),
    url(r'^contratista/perfil/quitar-formacion/(?P<formation_id>\d+)$', app_auth.views.delete_formation, name='del_contractor_formation'),

    url(r'^contratista/perfil/agregar-logro/$', app_auth.views.add_achievement, name='contractor_achievement'),
    url(r'^contratista/perfil/editar-logro/(?P<achievement_id>\d+)$', app_auth.views.edit_achievement, name='edit_contractor_ach'),
    url(r'^contratista/perfil/quitar-logro/(?P<achievement_id>\d+)$', app_auth.views.delete_achievement, name='del_contractor_ach'),

    url(r'^contratista/grupos/$', app_auth.views.contractor_groups, name='contractor_groups'),
    url(r'^contratista/grupos/(?P<group_id>\d+)/$', app_auth.views.group_members, name='group_members'),
    url(r'^contratista/grupos/(?P<group_id>\d+)/nuevo-miembro/$', app_auth.views.add_member, name='add_member'),
    url(r'^contratista/grupos/(?P<group_id>\d+)/editar-miembro/(?P<member_id>\d+)/$', app_auth.views.edit_member, name='edit_member'),

    url(r'^contratista/reportar-actividad/$', app_auth.views.load_report_form, name='report_form'),
    url(r'^contratista/reportar-actividad/(?P<intervention_id>\d+)$', app_auth.views.send_members, name='report_form'),

    url(r'^configuracion/', include('settings.urls', 'settings'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
