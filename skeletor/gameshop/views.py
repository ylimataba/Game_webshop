from django.shortcuts import render
from .models import Score, Game, Gamer, Developer
from .forms import RegistrationForm
from django.http import HttpResponseRedirect    
from django.contrib import auth                 
from django.core.context_processors import csrf 
from django.contrib.auth.decorators import login_required

def index(request):
    context = {'user':request.user}
    return render(request, 'gameshop/index.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    return render(request, 'gameshop/register.html', args)

@login_required(login_url='/')
def profile(request):
    context = {'user':request.user}
    return render(request, 'gameshop/profile.html', context)

def shop(request):
    games = Game.objects.all()
    context = {'games':games, 'user':request.user}
    return render(request, 'gameshop/shop.html', context)

@login_required(login_url='/')
def play(request):
    context = {}
    return render(request, 'gameshop/play.html', context)
