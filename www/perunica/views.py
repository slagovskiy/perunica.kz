import logging
from django.shortcuts import render
from django.http import HttpResponse
from perunica.apps.shop.models import Goods
from django.contrib.flatpages.models import FlatPage

log = logging.getLogger(__name__)

def index(request):
    try:
        page = FlatPage.objects.filter(title='INDEX')
        if len(page) == 0:
            page = FlatPage.objects.create(
                title='INDEX',
                content='FIRST PAGE'
            )
        else:
            page = page[0]
        goods = Goods.objects.all().filter(is_on_first=True, deleted=False)
        context = {
            'goods': goods,
            'content': page.content
        }
    except:
        context = {}
        log.error('Error get_index')
    return render(request, 'index.html', context)
