import logging
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Manager
import uuid

log = logging.getLogger(__name__)


def index(request):
    try:
        context = {}
        if 'Manager' not in request.session:
            return HttpResponseRedirect('/manager/login/')
        else:
            if request.session['Manager'] == None:
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
                request.session['Manager'] = {
                    'name': u[0].name,
                    'login': u[0].login,
                    'email': u[0].email
                }
                HttpResponseRedirect('/manager/')
        context = {}
    except:
        context = {}
        log.exception('Error get_index')
    return render(request, 'manager/login.html', context)


