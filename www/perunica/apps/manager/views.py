import logging
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Manager
from perunica.apps.shop.models import Order
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
        log.exception('Error get_index')
    return render(request, 'manager/login.html', context)


def logout(request):
    try:
        request.session['manager'] = None
        return HttpResponseRedirect('/manager/login/')
        context = {}
    except:
        context = {}
        log.exception('Error get_index')
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
        log.exception('Error get_index')
    return render(request, 'manager/order_table.html', context)


