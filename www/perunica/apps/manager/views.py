import logging
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User as UserManager
import uuid

log = logging.getLogger(__name__)


def index(request):
    try:
        context = {}
        if 'UserManager' not in request.session:
            return HttpResponseRedirect('/manager/login/')
        else:
            if request.session['UserManager'] == None:
                return HttpResponseRedirect('/manager/login/')
    except:
        context = {}
        log.exception('Error get_index')
    return render(request, 'manager/index.html', context)


def login(request):
    try:
        context = {}
    except:
        context = {}
        log.exception('Error get_index')
    return render(request, 'manager/login.html', context)


