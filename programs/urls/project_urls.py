from django.conf.urls import url

import programs.views.project_views as projects

urlpatterns = [
    url(r'^$', projects.list_projects, name='list_projects'),
    url(r'^nuevo', projects.create_project, name='new_project'),
    url(r'^ver/(?P<project_id>\d+)/', projects.view_project, name='view_project'),
    url(r'^editar/(?P<project_id>\d+)/', projects.update_project, name='edit_project'),
    #url(r'^bloquear/(?P<program_id>\d+)/', subprograms.toggle_lock, name='toggle_block_subprogram'),
]
