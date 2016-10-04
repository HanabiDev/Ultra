from django.conf.urls import url

import athletes.views as athletes


urlpatterns = [
    url(r'^$', athletes.list_athletes, name='list_athletes'),
    url(r'^nuevo', athletes.create_athlete, name='new_athlete'),
    url(r'^(?P<user_id>\d+)/ficha-deportiva/$', athletes.create_athlete_card, name='athlete_card'),
    url(r'^(?P<user_id>\d+)/ficha-deportiva/editar$', athletes.edit_athlete_card, name='edit_athlete_card'),
    url(r'^(?P<user_id>\d+)/ficha-social/$', athletes.create_athlete_socialcard, name='athlete_scard'),
    url(r'^(?P<user_id>\d+)/ficha-social/editar$', athletes.edit_athlete_socialcard, name='edit_athlete_scard'),
    url(r'^(?P<user_id>\d+)/resultado-deportivo/$', athletes.create_athlete_result, name='athlete_result'),
    url(r'^(?P<user_id>\d+)/resultado-deportivo/(?P<result_id>\d+)/editar$', athletes.edit_athlete_result, name='edit_athlete_result'),
    url(r'^(?P<user_id>\d+)/resultado-deportivo/(?P<result_id>\d+)/referente$', athletes.create_athlete_result_ref, name='athlete_result_ref'),
    #url(r'^(?P<user_id>\d+)/resultado-deportivo/(?P<result_id>\d+)/referente/(?P<ref_id>\d+)$', athletes.edit_athlete_result_ref, name='edit_athlete_result_ref'),
    url(r'^ver/(?P<user_id>\d+)/$', athletes.view_athlete, name='view_athlete'),
    url(r'^editar/(?P<user_id>\d+)/$', athletes.update_athlete, name='edit_athlete'),
    url(r'^municipios/$', athletes.filter_municipalities, name='municipalities'),
]
