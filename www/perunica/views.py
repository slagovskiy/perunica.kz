import logging
from django.shortcuts import render
from django.http import HttpResponse
from perunica.apps.shop.models import Goods
from django.contrib.flatpages.models import FlatPage
from perunica.utils.capcha import capcha_code, captcha_image


log = logging.getLogger(__name__)

def index(request):
    try:
        page_top = FlatPage.objects.filter(title='INDEX_TOP')
        if len(page_top) == 0:
            page_top = FlatPage.objects.create(
                title='INDEX_TOP',
                content='FIRST PAGE TOP'
            )
        else:
            page_top = page_top[0]
        page_bottom = FlatPage.objects.filter(title='INDEX_BOTTOM')
        if len(page_bottom) == 0:
            page_bottom = FlatPage.objects.create(
                title='INDEX_BOTTOM',
                content='FIRST PAGE BOTTOM'
            )
        else:
            page_bottom = page_bottom[0]
        goods = Goods.objects.all().filter(is_on_first=True, deleted=False)
        context = {
            'goods': goods,
            'page_top': page_top.content,
            'page_bottom': page_bottom.content
        }
    except:
        context = {}
        log.error('Error get_index')
    return render(request, 'index.html', context)


def capcha(request):
    request.session['CAPCHA_CODE'] = capcha_code(4)
    return captcha_image(request.session['CAPCHA_CODE'], 1)


def capcha_check(request, code):
    if 'CAPCHA_CODE' in request.session:
        if request.session['CAPCHA_CODE'] == str(code).upper():
            return HttpResponse('1', content_type="application/javascript")
        else:
            return HttpResponse('0', content_type="application/javascript")
    else:
        return HttpResponse('0', content_type="application/javascript")