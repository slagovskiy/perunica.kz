import logging
from django.shortcuts import render
from perunica.apps.shop.models import Menu, SubMenu
from django.http import HttpResponse


log = logging.getLogger(__name__)


def index(request):
    context = {}
    return render(request, 'index.html', context)


def get_menu(request, menu_slug):
    menu = Menu.objects.all().filter(slug=menu_slug)
    items = []
    context = {
        'menu': menu,
        'items': items
    }
    return render(request, 'index.html', context)