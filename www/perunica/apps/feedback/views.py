import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.core.mail import EmailMultiAlternatives
from perunica.settings import EMAIL_SUBJECT_PREFIX, DEFAULT_FROM_EMAIL
from perunica.apps.manager.models import Manager
from .models import Feedback
import uuid

log = logging.getLogger(__name__)


def index(request):
    try:
        context = {}
    except:
        context = {}
        log.exception('Error get_index')
    return render(request, 'feedback/index.html', context)


def save(request):
    try:
        if str(request.session['CAPCHA_CODE']).upper() == str(request.GET['capcha']).upper():
            fb = Feedback.objects.create(
                name = request.GET['fio'],
                email = request.GET['email'],
                phone = request.GET['phone'],
                comment = request.GET['comment']
            )
            fb.save()
            for u in Manager.objects.all().filter(deleted=False):
                try:
                    c = Context({'fb': fb})
                    subject = u'Новый отзыв #' + str(fb.id).format('%06d')
                    from_email = EMAIL_SUBJECT_PREFIX + ' <' + DEFAULT_FROM_EMAIL + '>'
                    to = u.email
                    text_content = loader.get_template('feedback/email_text.html').render(c)
                    html_content = loader.get_template('feedback/email_html.html').render(c)
                    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                except:
                    log.exception('Error send message')
            return HttpResponse('ok')
        else:
            log.warn('Wrong capcha')
            return HttpResponse('capcha')
    except:
        log.exception('Error save_feedback')
        return HttpResponse('error')