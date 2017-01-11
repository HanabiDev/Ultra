from django.conf.urls import url

import events.views as events

urlpatterns = [
    url(r'^$', events.list_events, name='list_events'),
    url(r'^nuevo', events.create_event, name='new_event'),
    url(r'^ver/(?P<event_id>\d+)/$', events.view_event, name='view_event'),
    url(r'^editar/(?P<event_id>\d+)/$', events.update_event, name='edit_event'),
    url(r'^(?P<event_id>\d+)/clasificacion/$', events.rank_event, name='rank_event'),
    url(r'^(?P<event_id>\d+)/reporte-clasificacion/$', events.rank_report, name='rank_report'),
]

