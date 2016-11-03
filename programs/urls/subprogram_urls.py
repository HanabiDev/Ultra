from django.conf.urls import url

import programs.views.subprogram_views as subprograms
import programs.views.project_views as projects

urlpatterns = [
    url(r'^$', subprograms.list_subprograms, name='list_subprograms'),
    url(r'^nuevo', subprograms.create_subprogram, name='new_subprogram'),
    url(r'^ver/(?P<subprogram_id>\d+)/$', subprograms.view_subprogram, name='view_subprogram'),
    url(r'^ver/(?P<subprogram_id>\d+)/mapa/$', subprograms.view_map, name='map'),
    url(r'^(?P<subprogram_id>\d+)/nuevo-proyecto/$', projects.create_project, name='proj'),
    url(r'^(?P<subprogram_id>\d+)/reporte/$', subprograms.report, name='subprog_report'),
    url(r'^editar/(?P<subprogram_id>\d+)/', subprograms.update_subprogram, name='edit_subprogram'),

    #url(r'^bloquear/(?P<program_id>\d+)/', subprograms.toggle_lock, name='toggle_block_subprogram'),
]
