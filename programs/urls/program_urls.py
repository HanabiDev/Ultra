from django.conf.urls import url

import programs.views.program_views as programs

urlpatterns = [
    url(r'^$', programs.list_programs, name='list_programs'),
    url(r'^nuevo', programs.create_program, name='new_program'),
    url(r'^ver/(?P<program_id>\d+)/', programs.view_program, name='view_program'),
    url(r'^editar/(?P<program_id>\d+)/', programs.update_program, name='edit_program'),
    url(r'^bloquear/(?P<program_id>\d+)/', programs.toggle_lock, name='toggle_block_program'),
]
