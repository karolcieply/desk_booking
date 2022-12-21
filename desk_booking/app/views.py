from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import SignUpForm
#from django.template import loader


def index(request):
    context = {
        'test': list(range(0,5)),
    }
    template = loader.get_template('desk_booking/index.html')
    return HttpResponse(template.render(context, request))

def login(request):
    
    # context = {
    #     'test': list(range(0,5)),
    # }
    # template = loader.get_template('desk_booking/login.html')
    
    form = SignUpForm()
    return render(request, 'desk_booking/login.html', {'form': form})
