import logging
from django.shortcuts import render
from perunica.apps.shop.models import Menu, SubMenu, Goods, GoodsGroup, GoodsLinkGroup, Order, OrderBody, OrderHistory
from perunica.utils.models import Global
from django.contrib.auth.models import User, AnonymousUser
from django.http import HttpResponse
from django.db import transaction
import uuid

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


def basket_edit(request):
    try:
        if 'basket' not in request.session:
            request.session['basket'] = []
        context = {}
    except:
        context = {}
        log.exception('Error get_basket')
    return render(request, 'shop/basket_edit.html', context)


def basket_delivery(request):
    try:
        if 'basket' not in request.session:
            request.session['basket'] = []
        context = {}
    except:
        context = {}
        log.exception('Error get_basket')
    return render(request, 'shop/basket_delivery.html', context)


def basket_confirm(request):
    try:
        if('fio' in request.GET):
            request.session['fio'] = request.GET['fio']
        if('phone' in request.GET):
            request.session['phone'] = request.GET['phone']
        if('email' in request.GET):
            request.session['email'] = request.GET['email']
        if('payment' in request.GET):
            request.session['payment'] = request.GET['payment']
        if('address' in request.GET):
            request.session['address'] = request.GET['address']
        if 'basket' not in request.session:
            request.session['basket'] = []
        context = {}
    except:
        context = {}
        log.exception('Error get_basket')
    return render(request, 'shop/basket_confirm.html', context)


def basket_ok(request):
    try:
        if 'basket' not in request.session:
            request.session['basket'] = []
        context = {}
    except:
        context = {}
        log.exception('Error get_basket')
    return render(request, 'shop/basket_ok.html', context)


def basket_data(request):
    try:
        if 'basket' not in request.session:
            request.session['basket'] = []
        order = []
        total_summ = 0
        gl = Global.objects.filter(active=True)
        if len(gl) > 0:
            gl = gl[0]
        else:
            gl = Global.objects.create()
        for item in request.session['basket']:
            summ = 0
            g = Goods.objects.get(id=item['id'])
            tmp = {
                'goods': g,
                'uuid': item['uuid'],
                'count': item['count'],
                'option': []
            }
            for _item in item['option']:
                o = Goods.objects.get(id=_item['id'])
                summ += o.price * _item['count']
                _tmp = {
                    'goods': o,
                    'uuid': _item['uuid'],
                    'count': _item['count']
                }
                tmp['option'].append(_tmp)
            summ += g.price * item['count']
            tmp['summ'] = summ
            total_summ += summ
            order.append(tmp)
        if total_summ >= gl.order_min_sum:
            next_step = True
        else:
            next_step = False
        request.session['total_sum'] = total_summ
        request.session['order_len'] = len(order)
        context = {
            'order': order,
            'total_summ': total_summ,
            'next_step': next_step
        }
    except:
        context = {}
        log.exception('Error get_basket')
    return render(request, 'shop/basket_data.html', context)


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
                    'uuid': uuid.uuid1().hex,
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
                        'uuid': uuid.uuid1().hex,
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
                            'uuid': uuid.uuid1().hex,
                            'count': 1,
                            'price': option1.price
                        }
                    )

                if int(_id[2])!=0:
                    option2 = Goods.objects.all().get(id=_id[2])
                    _tmp[0]['option'].append(
                        {
                            'id': option2.id,
                            'uuid': uuid.uuid1().hex,
                            'count': 1,
                            'price': option2.price
                        }
                    )
                if int(_id[3])!=0:
                    option3 = Goods.objects.all().get(id=_id[3])
                    _tmp[0]['option'].append(
                        {
                            'id': option3.id,
                            'uuid': uuid.uuid1().hex,
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


def basket_item_minus(request, uu):
    try:
        tmp = request.session['basket']
        if not tmp:
            tmp = []
        for item in tmp:
            if uu == item['uuid']:
                item['count'] -= 1
                request.session['basket'] = tmp
                return HttpResponse('ok')
        request.session['basket'] = tmp
        return HttpResponse('ok')
    except:
        log.exception('Error basket_item_minus')
        return HttpResponse('error')


def basket_item_plus(request, uu):
    try:
        tmp = request.session['basket']
        if not tmp:
            tmp = []
        for item in tmp:
            if uu == item['uuid']:
                item['count'] += 1
                request.session['basket'] = tmp
                return HttpResponse('ok')
        request.session['basket'] = tmp
        return HttpResponse('ok')
    except:
        log.exception('Error basket_item_minus')
        return HttpResponse('error')


def basket_item_delete(request, uu):
    try:
        tmp = request.session['basket']
        if not tmp:
            tmp = []
        for item in tmp:
            if uu == item['uuid']:
                tmp.remove(item)
                request.session['basket'] = tmp
                return HttpResponse('ok')
        request.session['basket'] = tmp
        return HttpResponse('ok')
    except:
        log.exception('Error basket_item_minus')
        return HttpResponse('error')


def basket_clear(request):
    try:
        request.session['basket'] = []
        return HttpResponse('ok')
    except:
        context = {}
        log.error('Error basket_clear')
        return HttpResponse('error')


@transaction.atomic
def basket_save(request):
    sid = transaction.savepoint()
    try:
        if 'basket' not in request.session:
            log.warn('no basket')
            transaction.savepoint_rollback(sid)
            return HttpResponse('error')

        if request.session['basket'] == []:
            log.warn('basket is empty')
            transaction.savepoint_rollback(sid)
            return HttpResponse('error')

        order = Order.objects.create(
            fio=request.session['fio'],
            phone=request.session['phone'],
            email=request.session['email'],
            address=request.session['address'],
            payment=request.session['payment'],
            uuid=uuid.uuid1().hex
        )
        order.save()

        order_history = OrderHistory.objects.create(
            order=order,
            status=1
        )
        order_history.save()

        for item in request.session['basket']:
            tmp_goods = Goods.objects.get(id=item['id'])
            order_body = OrderBody.objects.create(
                order=order,
                goods=tmp_goods,
                price=float(item['price']),
                count=float(item['count'])
            )
            option_i = 1
            for _item in item['option']:
                tmp_option = Goods.objects.get(id=_item['id'])
                log.warn(tmp_option)
                if option_i == 1:
                    order_body.option1 = tmp_option
                    option_i += 1
                if option_i == 2:
                    order_body.option2 = tmp_option
                    option_i += 1
                if option_i == 3:
                    order_body.option3 = tmp_option
                    option_i += 1
            order_body.save()

        request.session['basket'] = []
        transaction.savepoint_commit(sid)
        return HttpResponse('ok')
    except:
        transaction.savepoint_rollback(sid)
        log.exception('Error save order')
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