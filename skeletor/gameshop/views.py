from django.shortcuts import render
from .models import Game, User, Score

def index(request):
    context = {}
    return render(request, 'gameshop/index.html', context)

''' TODO write corresponding templates!

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

'''
