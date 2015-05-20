from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'perunica.apps.feedback.views.index', name='home'),
    url(r'^save/$', 'perunica.apps.feedback.views.save', name='save'),
]
