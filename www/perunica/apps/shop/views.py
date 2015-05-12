import logging
from django.shortcuts import render
from perunica.apps.shop.models import Menu, SubMenu, Goods, GoodsGroup, GoodsLinkGroup
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
        log.exception('Error get_index')
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
        log.exception('Error get_menu')
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
        log.exception('Error get_menu')
    return render(request, 'shop/menu.html', context)


def get_basket(request):
    try:
        if 'basket' not in request.session:
            request.session['basket'] = []
        summ = 0
        for item in request.session['basket']:
            summ += float(item['count'])*float(item['price'])
            for _item in item['option']:
                summ += float(_item['count'])*float(_item['price'])
        context = {
            'summ': summ,
        }
    except:
        context = {}
        log.exception('Error get_basket')
    return render(request, 'shop/basket.html', context)


def basket_add(request, id):
    try:
        _id = str(id).split('-')
        if len(_id)==1:
            goods = Goods.objects.all().get(id=_id[0])
            tmp = request.session['basket']
            if not tmp:
                tmp = []
            for item in tmp:
                if goods.id == item['id']:
                    item['count'] += 1
                    request.session['basket'] = tmp
                    return HttpResponse('ok')
            tmp.append(
                {
                    'id': goods.id,
                    'count': 1,
                    'price': goods.price,
                    'option': []
                }
            )
            request.session['basket'] = tmp
            return HttpResponse('ok')
        else:
            if len(_id)==4:
                goods = Goods.objects.all().get(id=_id[0])
                tmp = request.session['basket']
                if not tmp:
                    tmp = []
                _tmp = []
                _tmp.append(
                    {
                        'id': goods.id,
                        'count': 1,
                        'price': goods.price,
                        'option': []
                    }
                )
                if int(_id[1])!=0:
                    option1 = Goods.objects.all().get(id=_id[1])
                    _tmp[0]['option'].append(
                        {
                            'id': option1.id,
                            'count': 1,
                            'price': option1.price
                        }
                    )

                if int(_id[2])!=0:
                    option2 = Goods.objects.all().get(id=_id[2])
                    _tmp[0]['option'].append(
                        {
                            'id': option2.id,
                            'count': 1,
                            'price': option2.price
                        }
                    )
                if int(_id[3])!=0:
                    option3 = Goods.objects.all().get(id=_id[3])
                    _tmp[0]['option'].append(
                        {
                            'id': option3.id,
                            'count': 1,
                            'price': option3.price
                        }
                    )
                tmp.extend(_tmp)
                request.session['basket'] = tmp
                return HttpResponse('ok')
            else:
                return HttpResponse('error')
    except:
        log.exception('Error basket_add')
        return HttpResponse('error')


def basket_clear(request):
    try:
        request.session['basket'] = []
        return HttpResponse('ok')
    except:
        context = {}
        log.error('Error basket_clear')
        return HttpResponse('error')


def get_choice(request, id):
    try:
        goods = Goods.objects.all().get(id=id)
        choice = GoodsLinkGroup.objects.filter(group=goods.choice)[0].goods.all()
        title = GoodsLinkGroup.objects.filter(group=goods.choice)[0].group.title
        context = {
            'choice': choice,
            'title': title
        }
    except:
        context = {}
        log.exception('Error get_choice')
    return render(request, 'shop/choice.html', context)


def get_option(request, id):
    try:
        goods = Goods.objects.all().get(id=id)
        if goods.option1:
            option1 = GoodsLinkGroup.objects.filter(group=goods.option1)[0].goods.all()
            option1_title = GoodsLinkGroup.objects.filter(group=goods.option1)[0].group.title
        else:
            option1 = []
            option1_title = ''
        if goods.option2:
            option2 = GoodsLinkGroup.objects.filter(group=goods.option2)[0].goods.all()
            option2_title = GoodsLinkGroup.objects.filter(group=goods.option2)[0].group.title
        else:
            option2 = []
            option2_title = ''
        if goods.option3:
            option3 = GoodsLinkGroup.objects.filter(group=goods.option3)[0].goods.all()
            option3_title = GoodsLinkGroup.objects.filter(group=goods.option3)[0].group.title
        else:
            option3 = []
            option3_title = ''
        context = {
            'option1': option1,
            'option2': option2,
            'option3': option3,
            'option1_title': option1_title,
            'option2_title': option2_title,
            'option3_title': option3_title,
        }
    except:
        context = {}
        log.exception('Error get_option')
    return render(request, 'shop/option.html', context)