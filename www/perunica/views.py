import logging
from django.shortcuts import render
from django.http import HttpResponse
from perunica.apps.shop.models import Goods
from django.contrib.flatpages.models import FlatPage
from perunica.utils.capcha import capcha_code, captcha_image


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


def capcha(request):
    request.session['CAPCHA_CODE'] = capcha_code(4)
    return captcha_image(request.session['CAPCHA_CODE'], 1)


def capcha_check(request, code):
    data = '0'
    if 'CAPCHA_CODE' in request.session:
        if request.session['CAPCHA_CODE'] == str(code).upper():
            request.session['CAPCHA_CODE'] = capcha_code(4)
            return HttpResponse('1', content_type="application/javascript")
        else:
            request.session['CAPCHA_CODE'] = capcha_code(4)
            return HttpResponse('0', content_type="application/javascript")
    else:
        request.session['CAPCHA_CODE'] = capcha_code(4)
        return HttpResponse('0', content_type="application/javascript")