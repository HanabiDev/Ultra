from django.conf.urls import url

import athletes.views as athletes


urlpatterns = [
    url(r'^$', athletes.list_athletes, name='list_athletes'),
    url(r'^nuevo', athletes.create_athlete, name='new_athlete'),
    url(r'^ver/(?P<user_id>\d+)/', athletes.view_contractor, name='view_athlete'),
    url(r'^editar/(?P<user_id>\d+)/', athletes.update_athlete, name='edit_athlete'),
    url(r'^municipios/', athletes.filter_municipalities, name='municipalities'),
]
