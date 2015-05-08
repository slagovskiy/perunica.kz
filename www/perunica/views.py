import logging
from django.shortcuts import render
from django.http import HttpResponse
from perunica.apps.shop.models import Goods

log = logging.getLogger(__name__)

def index(request):
    try:
        goods = Goods.objects.all().filter(is_on_first=True, deleted=False)
        context = {
            'goods': goods
        }
    except:
        context = {}
        log.error('Error get_index')
    return render(request, 'index.html', context)
