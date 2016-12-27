from django.conf.urls import url

import athletes.views as athletes


urlpatterns = [
    url(r'^$', athletes.list_athletes, name='list_athletes'),
    url(r'^reporte-por-ligas/$', athletes.report_athletes, name='report_athletes'),
    url(r'^nuevo', athletes.create_athlete, name='new_athlete'),
    url(r'^(?P<user_id>\d+)/ficha-deportiva/$', athletes.create_athlete_card, name='athlete_card'),
    url(r'^(?P<user_id>\d+)/ficha-deportiva/editar$', athletes.edit_athlete_card, name='edit_athlete_card'),
    url(r'^(?P<user_id>\d+)/ficha-social/$', athletes.create_athlete_socialcard, name='athlete_scard'),
    url(r'^(?P<user_id>\d+)/ficha-social/editar$', athletes.edit_athlete_socialcard, name='edit_athlete_scard'),

    url(r'^(?P<user_id>\d+)/resultado-deportivo/$', athletes.create_athlete_result, name='athlete_result'),
    url(r'^(?P<user_id>\d+)/resultado-deportivo/(?P<result_id>\d+)/editar$', athletes.edit_athlete_result, name='edit_athlete_result'),
    url(r'^(?P<user_id>\d+)/resultado-deportivo/(?P<result_id>\d+)/referente$', athletes.create_athlete_result_ref, name='athlete_result_ref'),

    url(r'^(?P<user_id>\d+)/prueba/nueva$', athletes.create_athlete_test, name='athlete_test'),
    url(r'^(?P<user_id>\d+)/prueba/(?P<test_id>\d+)/editar$', athletes.edit_athlete_result, name='edit_athlete_test'),

    url(r'^(?P<user_id>\d+)/pruebas/refs/$', athletes.list_test_ref, name='athlete_ref_list'),
    url(r'^(?P<user_id>\d+)/pruebas/refs/nuevo$', athletes.create_test_ref, name='athlete_test_ref'),

    #url(r'^(?P<user_id>\d+)/pruebas/refs/(?P<ref_id>\d+)$', athletes.create_test_ref, name='edit_athlete_test_ref'),

    url(r'^(?P<user_id>\d+)/ficha-biomedica/$', athletes.create_biomedic_card, name='athlete_biomedic_card'),
    url(r'^(?P<user_id>\d+)/ficha-biomedica/(?P<tab_id>\d+)/valoracion-ffpb/$', athletes.create_SFPB_valoration, name='SFPBValoration'),
    url(r'^(?P<user_id>\d+)/ficha-biomedica/(?P<tab_id>\d+)/valoracion-antropometrica/$', athletes.create_antropometric_valoration, name='antropo'),
    url(r'^(?P<user_id>\d+)/ficha-biomedica/(?P<tab_id>\d+)/valoracion-psicodeportiva/$', athletes.create_psicologic_valoration, name='psico'),
    url(r'^(?P<user_id>\d+)/ficha-biomedica/(?P<tab_id>\d+)/valoracion-fisiologica/$', athletes.create_physiological_valoration, name='physio'),

    url(r'^(?P<user_id>\d+)/resultado-deportivo/(?P<result_id>\d+)/referente/(?P<ref_id>\d+)$', athletes.edit_athlete_result_ref, name='edit_athlete_result_ref'),

    url(r'^(?P<athlete_id>\d+)/opciones-reporte-evolucion/$', athletes.report_options, name='report_options'),
    url(r'^(?P<athlete_id>\d+)/reporte-evolucion/$', athletes.report, name='report'),

    url(r'^ver/(?P<user_id>\d+)/$', athletes.view_athlete, name='view_athlete'),
    url(r'^editar/(?P<user_id>\d+)/$', athletes.update_athlete, name='edit_athlete'),
    url(r'^municipios/$', athletes.filter_municipalities, name='municipalities'),
]
