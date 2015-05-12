from django.conf.urls import include, url
from django.contrib import admin
from perunica.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', 'perunica.apps.shop.views.index', name='home'),
    url(r'menu/(?P<menu_slug>[-\w]+)/(?P<sub_menu_slug>[-\w]+)/$', 'perunica.apps.shop.views.get_sub_menu', name='menu'),
    url(r'menu/(?P<menu_slug>[-\w]+)/$', 'perunica.apps.shop.views.get_menu', name='menu'),
    url(r'choice/(?P<id>[-\w]+)/$', 'perunica.apps.shop.views.get_choice', name='menu'),
    url(r'option/(?P<id>[-\w]+)/$', 'perunica.apps.shop.views.get_option', name='menu'),
    url(r'basket/add/(?P<id>[-\w]+)/$', 'perunica.apps.shop.views.basket_add', name='menu'),
    url(r'basket/data/$', 'perunica.apps.shop.views.basket_data', name='menu'),
    url(r'basket/edit/$', 'perunica.apps.shop.views.basket_edit', name='menu'),
    url(r'basket/clear/$', 'perunica.apps.shop.views.basket_clear', name='menu'),
    url(r'basket/$', 'perunica.apps.shop.views.get_basket', name='menu'),
]
