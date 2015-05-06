from django.conf.urls import include, url
from django.contrib import admin
from perunica.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', 'perunica.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT,
    }),


    url(r'^admin/', include(admin.site.urls)),
]
