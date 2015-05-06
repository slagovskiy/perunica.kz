import logging
from django import template

register = template.Library()
log = logging.getLogger(__name__)

@register.inclusion_tag('widgets/main_menu.html')
def widget_main_menu():
    try:
        from perunica.apps.shop.models import Menu
        main_menu = Menu.objects.all().order_by('sort', 'name').exclude(deleted=True)
    except:
        log.exception('Error get main menu')
    return {'main_menu': main_menu}


@register.inclusion_tag('widgets/sub_menu.html')
def widget_sub_menu(menu):
    try:
        from perunica.apps.shop.models import SubMenu
        from perunica.apps.shop.models import Menu
        sub_menu = SubMenu.objects.filter(menu=menu).order_by('sort', 'name').exclude(deleted=True)
    except:
        log.exception('Error get sub menu')
    return {'sub_menu': sub_menu}