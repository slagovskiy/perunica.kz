from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'perunica.apps.feedback.views.index', name='home'),
]
