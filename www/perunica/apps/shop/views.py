import logging
from django.shortcuts import render
from perunica.apps.shop.models import Menu, SubMenu
from django.http import HttpResponse


log = logging.getLogger(__name__)


def index(request):
    context = {}
    return render(request, 'shop/index.html', context)


def get_menu(request, menu_slug):
    try:
        menu = Menu.objects.all().filter(slug=menu_slug)[0]
        context = {
            'menu': menu
        }
    except:
        context = {}
        log.error('Error get_menu')
    return render(request, 'shop/index.html', context)