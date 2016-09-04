from django.conf.urls import url

import contractors.views as contractors


urlpatterns = [
    url(r'^nuevo', contractors.create_contractor, name='new'),
]
