import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from perunica.settings import EMAIL_SUBJECT_PREFIX, DEFAULT_FROM_EMAIL
from perunica.apps.manager.models import Manager
from .models import News
import uuid

log = logging.getLogger(__name__)


def index(request):
    try:
        news = News.objects.filter(deleted=False).order_by('-date')
        paginator = Paginator(news, 25)
        tmp = paginator.page(1)
        try:
            tmp = paginator.page(request.GET['page'])
        except:
            pass
        context = {
            'news': tmp
        }
    except:
        context = {}
        log.exception('Error get_index')
    return render(request, 'news/index.html', context)