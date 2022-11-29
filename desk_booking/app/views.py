from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from django.template import loader


def index(request):
    context = {
        'test': list(range(0,5)),
    }
    template = loader.get_template('desk_booking/index.html')
    return HttpResponse(template.render(context, request))