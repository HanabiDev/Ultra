from django.conf.urls import url

import athletes.views as athletes


urlpatterns = [
    url(r'^$', athletes.list_athletes, name='list_athletes'),
    url(r'^nuevo', athletes.create_athlete, name='new_athlete'),
    url(r'^(?P<user_id>\d+)/ficha-deportiva/$', athletes.create_athlete_card, name='athlete_card'),
    url(r'^(?P<user_id>\d+)/ficha-deportiva/editar$', athletes.edit_athlete_card, name='edit_athlete_card'),
    url(r'^ver/(?P<user_id>\d+)/$', athletes.view_contractor, name='view_athlete'),
    url(r'^editar/(?P<user_id>\d+)/$', athletes.update_athlete, name='edit_athlete'),
    url(r'^municipios/$', athletes.filter_municipalities, name='municipalities'),
]
