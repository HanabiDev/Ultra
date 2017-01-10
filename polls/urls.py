from django.conf.urls import url

import polls.views as polls

urlpatterns = [
    url(r'^$', polls.list_polls, name='list_polls'),
    url(r'^nueva', polls.create_poll, name='new_poll'),
    url(r'^ver/(?P<poll_id>\d+)/$', polls.view_poll, name='view_poll'),
    url(r'^editar/(?P<poll_id>\d+)/$', polls.update_poll, name='edit_poll'),
    url(r'^reporte/(?P<poll_id>\d+)/$', polls.report_poll, name='report_poll'),
    url(r'^bloquear/(?P<poll_id>\d+)/$', polls.toggle_lock, name='toggle_block_poll'),

    url(r'^(?P<poll_id>\d+)/nueva-pregunta/$', polls.create_question, name='poll_question'),
    url(r'^(?P<poll_id>\d+)/ver-pregunta/(?P<question_id>\d+)/$', polls.view_question, name='view_question'),
    url(r'^(?P<poll_id>\d+)/editar-pregunta/(?P<question_id>\d+)/$', polls.update_question, name='edit_question'),

    url(r'^(?P<poll_id>\d+)/pregunta/(?P<question_id>\d+)/nueva-opcion/$', polls.create_option, name='poll_option'),
    url(r'^(?P<poll_id>\d+)/pregunta/(?P<question_id>\d+)/editar-opcion/(?P<option_id>\d+)/$', polls.update_option, name='edit_option'),
]

