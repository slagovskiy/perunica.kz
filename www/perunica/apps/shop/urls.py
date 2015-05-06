from django.conf.urls import include, url
from django.contrib import admin
from perunica.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', 'perunica.apps.shop.views.index', name='home'),
    url(r'menu/(?P<menu_slug>[-\w]+)/(?P<sub_menu_slug>[-\w]+)/$', 'perunica.apps.shop.views.get_sub_menu', name='menu'),
    url(r'menu/(?P<menu_slug>[-\w]+)/$', 'perunica.apps.shop.views.get_menu', name='menu'),
]
