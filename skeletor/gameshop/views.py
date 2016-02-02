from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect    
from django.contrib import auth                 
from django.core.context_processors import csrf 
from django.contrib.auth.decorators import login_required
from .models import Score, Game, Gamer, Developer
from .forms import RegistrationForm, PaymentForm
from hashlib import md5

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
    context = {'game':game}
    return render(request, 'gameshop/play.html', context)

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
                user.gamer.library.add(game)
                user.save()
            else:
                template = 'gameshop/shop_error.html'
        elif res=='cancel':
            template = 'gameshop/shop_cancel.html'
        elif res=='error':
            template = 'gameshop/shop_error.html'
        context['res'] = res
    return render(request, template, context)

