from django.shortcuts import render
from .models import Game, User, Score #TODO import correct models
#from django.contrib.auth.decorators import login_required

#@login_required(login_url='login')
def index(request):
    if not request.user.is_authenticated():
        context = {'user':False}
    else:
        context = {'user':True}
    return render(request, 'gameshop/index.html', context)

def register(request):
    context = {}
    return render(request, 'gameshop/register.html', context)

def profile(request):
    context = {}
    return render(request, 'gameshop/profile.html', context)

def shop(request):
    context = {}
    return render(request, 'gameshop/shop.html', context)

def play(request):
    context = {}
    return render(request, 'gameshop/play.html', context)


