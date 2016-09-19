from django.conf.urls import url

import app_auth.views as app_auth


urlpatterns = [
    #url(r'^$', athletes.list_athletes, name='list_athletes'),
    url(r'^recuperar-clave/$', app_auth.restore_password, name='restore_password'),
    #url(r'^ver/(?P<user_id>\d+)/', athletes.view_contractor, name='view_athlete'),
    #url(r'^editar/(?P<user_id>\d+)/', athletes.update_athlete, name='edit_athlete'),
    #url(r'^municipios/', athletes.filter_municipalities, name='municipalities'),
]