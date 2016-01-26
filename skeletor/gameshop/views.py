from django.shortcuts import render
from .models import Score, Game, Gamer, Developer
from .forms import RegistrationForm, PaymentForm
from django.http import HttpResponseRedirect    
from django.contrib import auth                 
from django.core.context_processors import csrf 
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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
    form = PaymentForm
    games = Game.objects.all()
    context = {'games':games, 'user':request.user, 'form':form}
    return render(request, 'gameshop/shop.html', context)

@login_required(login_url='/')
def play(request,game_id):
    game=get_object_or_404(Game,id=game_id)
    context = {'game':game}
    return render(request, 'gameshop/play.html', context)

def payment(request):
    if request.method == 'GET':
        res=request.GET.get('result')
        if res=='success':
            template = 'gameshop/shop_success.html'
            game_id=request.GET.get('game_id')
            game=Game.objects.get(id=game_id)
            user=request.user
            user.gamer.library.add(game)
            user.save()
        elif res=='cancel':
            template = 'gameshop/shop_cancel.html'
        elif res=='success':
            template = 'gameshop/shop_error.html'
    context={'res':res}
    return render(request, template, context)


