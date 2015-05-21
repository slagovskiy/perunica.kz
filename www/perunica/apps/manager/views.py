import logging
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Manager
from perunica.apps.shop.models import Order, OrderBody, OrderHistory, Goods
from perunica.apps.feedback.models import Feedback
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
        print = 'no'
        if 'print' in request.GET:
            print = request.GET['print']
        context = {
            'order': order,
            'print': print
        }
    except:
        context = {}
        log.exception('Error order_edit')
    return render(request, 'manager/order_edit.html', context)


def order_setstatus(request, id):
    try:
        if int(request.GET['status']) < 4:
            order = Order.objects.get(id=id)
            history = OrderHistory.objects.create(
                order = order,
                status = int(request.GET['status']) + 1
            )
            history.save()
        return HttpResponse('ok')
    except:
        log.exception('Error order_setstatus')
        return HttpResponse('error')


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


def orderbody_editoption(request, id, option):
    try:
        orderbody = OrderBody.objects.get(id=id)
        goods = Goods.objects.filter(deleted=False)
        context = {
            'orderbody': orderbody,
            'goods': goods,
            'option': option
        }
    except:
        context = {}
        log.exception('Error orderbosy_edit')
    return render(request, 'manager/orderbody_editoption.html', context)


def orderbody_saveoption(request, id):
    try:
        orderbody = OrderBody.objects.get(id=id)
        goods = Goods.objects.get(id=request.GET['id'])
        if request.GET['option']=='1':
            orderbody.option1 = goods
            orderbody.count_o1 = request.GET['count']
            orderbody.price_o1 = request.GET['price']
        elif request.GET['option']=='2':
            orderbody.option2 = goods
            orderbody.count_o2 = request.GET['count']
            orderbody.price_o2 = request.GET['price']
        else:
            orderbody.option3 = goods
            orderbody.count_o3 = request.GET['count']
            orderbody.price_o3 = request.GET['price']
        orderbody.save()
        return HttpResponse(orderbody.order.id)
    except:
        log.exception('Error orderbosy_edit')
        return HttpResponse('error')


def feedback(request):
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
    return render(request, 'manager/feedback.html', context)


def feedback_table(request):
    try:
        fb = Feedback.objects.all().order_by('-date')
        paginator = Paginator(fb, 3)
        tmp = paginator.page(1)
        try:
            tmp = paginator.page(request.GET['page'])
            log.warn(request.GET['page'])
        except:
            pass
        context = {
            'fb': tmp
        }
    except:
        context = {}
        log.exception('Error order_table')
    return render(request, 'manager/feedback_table.html', context)
