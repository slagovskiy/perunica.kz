import logging
from django.shortcuts import render
from perunica.apps.shop.models import Menu, SubMenu, Goods
from django.http import HttpResponse


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
    return render(request, 'shop/index.html', context)


def get_menu(request, menu_slug):
    try:
        menu = Menu.objects.all().filter(slug=menu_slug)[0]
        goods = Goods.objects.all().filter(menu=menu, deleted=False)
        context = {
            'menu': menu,
            'goods': goods
        }
    except:
        context = {}
        log.error('Error get_menu')
    return render(request, 'shop/menu.html', context)


def get_sub_menu(request, menu_slug, sub_menu_slug):
    try:
        menu = Menu.objects.all().filter(slug=menu_slug)[0]
        sub_menu = SubMenu.objects.all().filter(slug=sub_menu_slug)[0]
        goods = Goods.objects.all().filter(sub_menu=sub_menu, deleted=False)
        context = {
            'menu': menu,
            'sub_menu': sub_menu,
            'goods': goods
        }
    except:
        context = {}
        log.error('Error get_menu')
    return render(request, 'shop/menu.html', context)


def get_basket(request):
    try:
        '''
        request.session['basket'] = [
            {
                'id': 2,
                'count': 3,
                'price': 1200
            },
            {
                'id': 3,
                'count': 1,
                'price': 500
            },
            {
                'id': 6,
                'count': 2,
                'price': 250
            },
        ]
        '''
        summ = 0
        for item in request.session['basket']:
            summ = summ + item['count']*item['price']
        context = {
            'summ': summ,
        }
    except:
        context = {}
        log.error('Error get_basket')
    return render(request, 'shop/basket.html', context)


def basket_add(request, id):
    try:
        goods = Goods.objects.all().filter(id=id)[0]
        tmp = request.session['basket']
        if not tmp:
            tmp = []
        tmp.append(
            {
                'id': goods.id,
                'count': 1,
                'price': goods.price
            }
        )
        request.session['basket'] = tmp
        return HttpResponse('ok')
    except:
        context = {}
        log.error('Error basket_add')
        return HttpResponse('error')