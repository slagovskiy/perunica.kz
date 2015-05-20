import logging
from django.shortcuts import render
import uuid

log = logging.getLogger(__name__)


def index(request):
    try:
        context = {}
    except:
        context = {}
        log.exception('Error get_index')
    return render(request, 'feedback/index.html', context)
