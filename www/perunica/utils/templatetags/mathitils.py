# -*- coding: utf-8 -*-
from django import template
register = template.Library()

@register.filter
def mul(value, arg):
    return value * arg

@register.filter
def div(value, arg):
    return value / arg

@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def fmul(value, arg):
    return float(value) * float(arg)

@register.filter
def fdiv(value, arg):
    return float(value) / float(arg)

@register.filter
def fsub(value, arg):
    return float(value) - float(arg)
