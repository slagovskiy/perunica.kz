from django.conf.urls import include, url
from django.contrib import admin
from perunica.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', 'perunica.apps.manager.views.index', name='home'),
    url(r'login/$', 'perunica.apps.manager.views.login', name='login'),
]
