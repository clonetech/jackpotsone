from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils import timezone
from . models import Punter, Hexabet, Jackpot
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site


def home(request):
    template_name = 'home.html'
    return render(request, 'home.html')


def welcome(request):
    template_name = 'welcome.html'
    return render(request, 'welcome.html')

def payment(request):
    template_name = 'payment.html'
    return render(request, 'payment.html')

def punter(request):

    model = Punter

    template_name = 'punter.html'

    args = {}

    punter = Punter.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:2]


    args ['punter'] = punter

    return render(request, 'punter.html', args)


def jackpot(request):

    model = Jackpot

    template_name = 'jackpot.html'

    args = {}

    jackpot = Jackpot.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:17]


    args ['jackpot'] = jackpot

    return render(request, 'jackpot.html', args)


def hexabet(request):

    model = Hexabet

    template_name = 'hexabet.html'

    args = {}

    hexabet = Hexabet.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:6]


    args ['hexabet'] = hexabet

    return render(request, 'hexabet.html', args)


def results(request):

    template_name = 'results.html'

    args = {}

    results_teams = Hexabet.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[6:24]


    args ['results_teams'] = grouped(results_teams, 6)

    return render(request, 'results.html', args)


def grouped(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            return redirect('/welcome')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
