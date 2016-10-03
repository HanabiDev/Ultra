from django.conf.urls import url

import settings.views as settings


urlpatterns = [
    url(r'^$', settings.home, name='settings_home'),
    #url(r'^nuevo', athletes.create_athlete, name='new_athlete'),
    #url(r'^ver/(?P<user_id>\d+)/', athletes.view_contractor, name='view_athlete'),
    #url(r'^editar/(?P<user_id>\d+)/', athletes.update_athlete, name='edit_athlete'),
    #url(r'^municipios/', athletes.filter_municipalities, name='municipalities'),
]
