from django.conf.urls import url

import contractors.views as contractors


urlpatterns = [
    url(r'^$', contractors.list_contractors, name='list_contractors'),
    url(r'^nuevo', contractors.create_contractor, name='new_contractor'),
    url(r'^ver/(?P<user_id>\d+)/', contractors.view_contractor, name='view_contractor'),
    url(r'^editar/(?P<user_id>\d+)/$', contractors.update_contractor, name='edit_contractor'),
    url(r'^editar/(?P<user_id>\d+)/cambiar-clave/$', contractors.update_password, name='pass'),
    url(r'^bloquear/(?P<user_id>\d+)/', contractors.toggle_lock, name='toggle_block_contractor'),
]
