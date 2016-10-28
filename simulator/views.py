from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from simulator.forms import UserForm
from simulator.models import Instrument, Position
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import json
from googlefinance import getQuotes


def home(request):
    return render(request, 'home.html')

def getstockdata_views(request):
    
    query_str = str(request.GET['query'])
    print(query_str)

    p = json.dumps(getQuotes(query_str), indent=2)    
    print(p)
    return HttpResponse(p, content_type="application/json")



def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            return render(request, 'home.html')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form':form})


def signedup(request):
    return render(request, 'signedup.html')


def profile(request):
    # How do I access the user data in the request?
    print request.POST
    return render(request, 'profile.html')
