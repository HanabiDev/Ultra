from django.conf.urls import url

import programs.views.subprogram_views as subprograms

urlpatterns = [
    url(r'^$', subprograms.list_subprograms, name='list_subprograms'),
    url(r'^nuevo', subprograms.create_subprogram, name='new_subprogram'),
    url(r'^ver/(?P<program_id>\d+)/', subprograms.view_subprogram, name='view_subprogram'),
    url(r'^editar/(?P<program_id>\d+)/', subprograms.update_subprogram, name='edit_subprogram'),
    #url(r'^bloquear/(?P<program_id>\d+)/', subprograms.toggle_lock, name='toggle_block_subprogram'),
]
