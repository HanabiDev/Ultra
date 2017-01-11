from django.conf.urls import url

import main_site.views as site

urlpatterns = [
    url(r'^$', site.home, name='home'),
    url(r'^encuestas/$', site.list_polls, name='polls'),
    url(r'^encuestas/(?P<poll_id>\d+)/responder/$', site.answer_poll, name='fill_poll'),
    url(r'^eventos/$', site.list_events, name='events'),
    url(r'^eventos/(?P<event_id>\d+)/$', site.answer_poll, name='event'),
    url(r'^eventos/(?P<event_id>\d+)/inscripcion/$', site.event_suscribe, name='suscribe'),
]

