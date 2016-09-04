from django.conf.urls import url

import contractors.views as contractors


urlpatterns = [
    url(r'^$', contractors.list_contractors, name='list'),
    url(r'^nuevo', contractors.create_contractor, name='new'),
    url(r'^ver/(?P<user_id>\d+)/', contractors.view_contractor, name='view'),
    url(r'^editar/(?P<user_id>\d+)/', contractors.update_contractor, name='edit'),
]
