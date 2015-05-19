import logging
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Manager
from perunica.apps.shop.models import Order, OrderBody, OrderHistory, Goods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import uuid

log = logging.getLogger(__name__)


def index(request):
    try:
        context = {}
        if 'manager' not in request.session:
            return HttpResponseRedirect('/manager/login/')
        else:
            if 'login' not in request.session['manager']:
                return HttpResponseRedirect('/manager/login/')
    except:
        context = {}
        log.exception('Error get_index')
    return render(request, 'manager/index.html', context)


def login(request):
    try:
        if 'username' in request.POST and 'password' in request.POST:
            u = Manager.objects.filter(login=request.POST['username'], password=request.POST['password'], deleted=False)
            if len(u)>0:
                request.session['manager'] = {
                    'name': u[0].name,
                    'login': u[0].login,
                    'email': u[0].email,
                }
                return HttpResponseRedirect('/manager/')
        context = {}
    except:
        context = {}
        log.exception('Error login')
    return render(request, 'manager/login.html', context)


def logout(request):
    try:
        request.session['manager'] = None
        return HttpResponseRedirect('/manager/login/')
        context = {}
    except:
        context = {}
        log.exception('Error logout')
    return render(request, 'manager/login.html', context)


def order_table(request):
    try:
        desc = '-id'
        if 'desc' in request.GET:
            desc = request.GET['desc']
        orders = Order.objects.all().order_by(desc)
        paginator = Paginator(orders, 50)
        tmp = paginator.page(1)
        try:
            tmp = paginator.page(request.GET['page'])
            log.warn(request.GET['page'])
        except:
            pass
        context = {
            'orders': tmp,
            'desc': desc
        }
    except:
        context = {}
        log.exception('Error order_table')
    return render(request, 'manager/order_table.html', context)


def order_open(request, id):
    try:
        order = Order.objects.get(id=id)
        context = {
            'order': order
        }
    except:
        context = {}
        log.exception('Error order_edit')
    return render(request, 'manager/order_edit.html', context)


def orderbody_edit(request, id):
    try:
        orderbody = OrderBody.objects.get(id=id)
        goods = Goods.objects.filter(deleted=False)
        context = {
            'orderbody': orderbody,
            'goods': goods
        }
    except:
        context = {}
        log.exception('Error orderbosy_edit')
    return render(request, 'manager/orderbody_edit.html', context)


def orderbody_save(request, id):
    try:
        orderbody = OrderBody.objects.get(id=id)
        goods = Goods.objects.get(id=request.GET['id'])
        orderbody.goods = goods
        orderbody.count = request.GET['count']
        orderbody.price = request.GET['price']
        orderbody.save()
        return HttpResponse(orderbody.order.id)
    except:
        log.exception('Error orderbosy_edit')
        return HttpResponse('error')


