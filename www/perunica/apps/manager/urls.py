from django.conf.urls import include, url
from django.contrib import admin
from perunica.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', 'perunica.apps.manager.views.index', name='home'),
    url(r'login/$', 'perunica.apps.manager.views.login', name='login'),
    url(r'logout/$', 'perunica.apps.manager.views.logout', name='logout'),
    url(r'orders/$', 'perunica.apps.manager.views.order_table', name='orders'),
    url(r'order/(?P<id>[-\w]+)/$', 'perunica.apps.manager.views.order_open', name='order'),
    url(r'order/setstatus/(?P<id>[-\w]+)/$', 'perunica.apps.manager.views.order_setstatus', name='order'),
    url(r'orderbody/edit/(?P<id>[-\w]+)/$', 'perunica.apps.manager.views.orderbody_edit', name='orderbody'),
    url(r'orderbody/save/(?P<id>[-\w]+)/$', 'perunica.apps.manager.views.orderbody_save', name='orderbody'),
    url(r'orderbody/editoption/(?P<id>[-\w]+)/(?P<option>[-\w]+)/$', 'perunica.apps.manager.views.orderbody_editoption', name='orderbody'),
    url(r'orderbody/saveoption/(?P<id>[-\w]+)/$', 'perunica.apps.manager.views.orderbody_saveoption', name='orderbody'),
]
