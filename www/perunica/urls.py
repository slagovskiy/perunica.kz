from django.conf.urls import include, url
from django.contrib import admin
from perunica.settings import MEDIA_ROOT


admin.site.site_header = 'ПЕРУНИЦА - Администрирование'

urlpatterns = [
    url(r'^$', 'perunica.views.index', name='home'),
    url(r'^shop/', include('perunica.apps.shop.urls')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT,
    }),


    url(r'^admin/', include(admin.site.urls)),
]
