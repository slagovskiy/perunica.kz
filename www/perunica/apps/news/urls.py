from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'perunica.apps.news.views.index', name='home'),
]

