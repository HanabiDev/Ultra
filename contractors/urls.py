from django.conf.urls import url

import contractors.views as contractors


urlpatterns = [
    url(r'^$', contractors.list_contractors, name='list_contractors'),
    url(r'^nuevo', contractors.create_contractor, name='new_contractor'),
    url(r'^ver/(?P<user_id>\d+)/', contractors.view_contractor, name='view_contractor'),
    url(r'^editar/(?P<user_id>\d+)/$', contractors.update_contractor, name='edit_contractor'),
    url(r'^editar/(?P<user_id>\d+)/nuevo-item-formacion/$', contractors.add_formation, name='add_formation'),
    url(r'^editar/(?P<user_id>\d+)/editar-item-formacion/(?P<formation_id>\d+)/$', contractors.edit_formation, name='edit_formation'),
    url(r'^editar/(?P<user_id>\d+)/eliminar-item-formacion/(?P<formation_id>\d+)/$', contractors.delete_formation, name='delete_formation'),
    url(r'^editar/(?P<user_id>\d+)/nuevo-logro-deportivo/$', contractors.add_achievement, name='add_achievement'),
    url(r'^editar/(?P<user_id>\d+)/editar-logro-deportivo/(?P<achievement_id>\d+)/$', contractors.edit_achievement, name='edit_achievement'),
    url(r'^editar/(?P<user_id>\d+)/eliminar-logro-deportivo/(?P<achievement_id>\d+)/$', contractors.delete_achievement, name='delete_achievement'),
    url(r'^editar/(?P<user_id>\d+)/cambiar-clave/$', contractors.update_password, name='pass'),
    url(r'^bloquear/(?P<user_id>\d+)/', contractors.toggle_lock, name='toggle_block_contractor'),
]
