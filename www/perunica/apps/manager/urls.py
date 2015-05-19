from django.conf.urls import include, url
from django.contrib import admin
from perunica.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', 'perunica.apps.manager.views.index', name='home'),
    url(r'login/$', 'perunica.apps.manager.views.login', name='login'),
    url(r'logout/$', 'perunica.apps.manager.views.logout', name='logout'),
    url(r'orders/$', 'perunica.apps.manager.views.order_table', name='logout'),
]
