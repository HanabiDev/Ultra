from django.conf.urls import url

import programs.views.program_views as programs
import programs.views.subprogram_views as subprograms

urlpatterns = [
    url(r'^$', programs.list_programs, name='list_programs'),
    url(r'^nuevo', programs.create_program, name='new_program'),
    url(r'^ver/(?P<program_id>\d+)/$', programs.view_program, name='view_program'),
    url(r'^ver/(?P<program_id>\d+)/mapa/$', programs.view_program_map, name='view_program_map'),
    url(r'^(?P<program_id>\d+)/nuevo-subprograma/$', subprograms.create_subprogram, name='program_sub'),
    url(r'^editar/(?P<program_id>\d+)/$', programs.update_program, name='edit_program'),
    url(r'^bloquear/(?P<program_id>\d+)/$', programs.toggle_lock, name='toggle_block_program'),
]
