from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse   
from django.contrib import auth                 
from django.core.context_processors import csrf 
from django.contrib.auth.decorators import login_required
from .models import Score, Game, Gamer, Developer, GameSave
from .forms import RegistrationForm, PaymentForm, GameForm
from hashlib import md5
from django.contrib.auth.models import User
import json

def index(request):
    context = {'user':request.user}
    return render(request, 'gameshop/index.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {}
    context.update(csrf(request))
    context['form'] = RegistrationForm()
    return render(request, 'gameshop/register.html', context)

@login_required(login_url='/')
def profile(request):
    context = {'user':request.user}
    return render(request, 'gameshop/profile.html', context)

def shop(request):
    if request.method == 'POST' and request.user.is_authenticated():
        game=get_object_or_404(Game,id=request.POST.get('game_id'))
        secret_key = '6cd118b1432bf22942d93d784cd17084' # pitää muuttaa http://payments.webcourse.niksula.hut.fi/key/
        pid = game.name
        sid = 'tester' # pitää muuttaa http://payments.webcourse.niksula.hut.fi/key/
        amount = str(game.price)
        checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
        m = md5(checksumstr.encode("ascii"))
        checksum = m.hexdigest()
        data = {
                'amount' : amount,
                'checksum' : checksum,
                'pid' : pid,
                'sid' : sid, 
                'success_url' : 'http://localhost:8000/payment',
                'cancel_url' : 'http://localhost:8000/payment',
                'error_url' : 'http://localhost:8000/payment',
                }
        form = PaymentForm(None, initial=data)
        context = {'form':form}
        template = 'gameshop/payment.html'
    else:
        games = Game.objects.all()
        context = {'games':games, 'user':request.user}
        template = 'gameshop/shop.html'
    return render(request, template, context)

@login_required(login_url='/')
def play(request,game_id):
    game=get_object_or_404(Game,id=game_id)
    user = request.user
    if game in user.gamer.library.all():
        if request.is_ajax():
            if request.GET.get('messageType')=='SCORE':
                points = request.GET.get('score')
                scr = Score(points=points, game=game, user=user)
                scr.save()
                response_data = {'message': 'SUCCESS'}
                json_data = json.dumps(response_data)
                return HttpResponse(json_data, content_type="application/json")

            elif request.GET.get('messageType')=='SAVE':
                gameState = request.GET.get('gameState')
                saving=GameSave(gameState=gameState, game=game, user=user)
                saving.save()
                response_data = {'message': 'SUCCESS'}
                json_data = json.dumps(response_data)
                return HttpResponse(json_data, content_type="application/json")

            elif request.GET.get('messageType')=='LOAD_REQUEST':
                saving = get_list_or_404(GameSave, game=game, user=user)[0]
                gameState = saving.gameState
                response_data = {'messageType': 'LOAD', 'gameState': json.loads(gameState)}
                json_data = json.dumps(response_data)
                return HttpResponse(json_data, content_type="application/json")
            else: 
                scores = Score.objects.filter(game=game)[:10]
                context = {'game':game, 'scores':scores}
                return render(request, 'gameshop/game_scores.html', context)
        else:
            scores = Score.objects.filter(game=game)[:10]
            context = {'game':game, 'scores':scores}
            return render(request, 'gameshop/play.html', context)
    else:
        return HttpResponseRedirect('/')

def payment(request):
    context = {}
    if request.method == 'GET':
        context.update(csrf(request))
        res=request.GET.get('result')
        if res=='success':
            game_name = request.GET.get('pid')
            ref = request.GET.get('ref')
            secret_key = '6cd118b1432bf22942d93d784cd17084' # pitää muutaa http://payments.webcourse.niksula.hut.fi/key/
            checksumstr = "pid={}&ref={}&result={}&token={}".format(game_name, ref, res, secret_key)
            m = md5(checksumstr.encode('ascii'))
            checksum = m.hexdigest()
            if checksum == request.GET.get('checksum'):
                game = get_object_or_404(Game, name=game_name)
                template = 'gameshop/shop_success.html'
                user=request.user
                user.gamer.addGame(game)
            else:
                template = 'gameshop/shop_error.html'
        elif res=='cancel':
            template = 'gameshop/shop_cancel.html'
        elif res=='error':
            template = 'gameshop/shop_error.html'
        context['res'] = res
    return render(request, template, context)

def developer(request):
    user = request.user
    context = {'user' : user}
    if hasattr(user, 'developer'):
        inventory = user.developer.inventory.all()
        context['inventory'] = inventory
    template = 'gameshop/developer.html'
    return render(request, template, context)

def add_game(request):
    user = request.user
    if hasattr(user, 'developer'):
        if request.method == 'POST':
            form = GameForm(request.POST)
            if form.is_valid():
                game = form.save(commit=False)
                game.game_developer = request.user
                game.save()
                return HttpResponseRedirect('/developer')

        form = GameForm()
        context = {'form' : form}
        return render(request, 'gameshop/add_game.html', context)
    else:
        return HttpResponseRedirect('/')

def modify_game(request, game_id):
    user = request.user
    game = get_object_or_404(Game, id=game_id)
    if hasattr(user, 'developer'):
        if game in user.developer.inventory.all():
            form = GameForm(request.POST or None, instance = game)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/developer')
            else:
                context = {'form' : form, 'game_id' : game_id}
                template = 'gameshop/modify_game.html'
                return render(request, template, context)
    return HttpResponseRedirect('/')

def remove_game(request, game_id):
    user=request.user
    game=get_object_or_404(Game, id=game_id)
    if hasattr(user, 'developer'):
        if game in user.developer.inventory.all():
            game.delete()
    return HttpResponseRedirect('/developer')
