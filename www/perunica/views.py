import logging
from django.shortcuts import render
from django.http import HttpResponse

log = logging.getLogger(__name__)

def index(request):
    context = {}
    return render(request, 'index.html', context)
