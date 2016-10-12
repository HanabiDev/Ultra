from django.conf.urls import url

import settings.views as settings


urlpatterns = [
    url(r'^$', settings.home, name='settings_home'),
    
    url(r'^deportes/$', settings.sports_index, name='sports_index'),
    url(r'^deportes/nuevo/$', settings.create_sport, name='new_sport'),
	url(r'^deportes/ver/(?P<sport_id>\d+)/$', settings.view_sport, name='view_sport'),
	url(r'^deportes/editar/(?P<sport_id>\d+)/$', settings.edit_sport, name='edit_sport'),
	url(r'^deportes/eliminar/(?P<sport_id>\d+)/$', settings.delete_sport, name='delete_sport'),
    url(r'^deportes/(?P<sport_id>\d+)/nueva-liga/$', settings.create_league, name='new_sport_league'),


	url(r'^ligas/$', settings.leagues_index, name='leagues_index'),
    url(r'^ligas/nueva/$', settings.create_league, name='new_league'),
	url(r'^ligas/ver/(?P<league_id>\d+)/$', settings.view_league, name='view_league'),
	url(r'^ligas/editar/(?P<league_id>\d+)/$', settings.edit_league, name='edit_league'),
	url(r'^ligas/eliminar/(?P<league_id>\d+)/$', settings.delete_league, name='delete_league'),
	url(r'^ligas/(?P<league_id>\d+)/nuevo-club/$', settings.create_club, name='new_league_club'),


	url(r'^clubes/$', settings.clubs_index, name='clubs_index'),
    url(r'^clubes/nuevo/$', settings.create_club, name='new_club'),
	url(r'^clubes/ver/(?P<club_id>\d+)/$', settings.view_club, name='view_club'),
	url(r'^clubes/editar/(?P<club_id>\d+)/$', settings.edit_club, name='edit_club'),
	url(r'^clubes/eliminar/(?P<club_id>\d+)/$', settings.delete_club, name='delete_club'),
    
    #url(r'^editar/(?P<user_id>\d+)/', athletes.update_athlete, name='edit_athlete'),
    #url(r'^municipios/', athletes.filter_municipalities, name='municipalities'),
]
