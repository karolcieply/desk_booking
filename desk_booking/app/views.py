from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .forms import SignUpForm
from django.contrib.auth import authenticate, login

def index(request):
    context = {
        'test': list(range(0,5)),
    }
    template = loader.get_template('desk_booking/index.html')
    return HttpResponse(template.render(context, request))


 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})