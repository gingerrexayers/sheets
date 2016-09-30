from django.shortcuts import render, redirect
from .models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'loginreg/index.html')

def register(request):
    if request.method=='POST':
        result = User.manager.register(request.POST)

        if result[0]:
            request.session['id'] = result[1].id
            return redirect(reverse('login:success'))
        else:
            for e in result[1]:
                messages.error(request, e)
            return redirect(reverse('login:index'))

def login(request):
    if request.method=='POST':
        result = User.manager.login(request.POST)
        if result[0]:
            request.session['id'] = result[1].id
            return redirect(reverse('login:success'))
        else:
            for e in result[1]:
                messages.error(request, e)
            return redirect(reverse('login:index'))

def logout(request):
    request.session.pop('id')
    return redirect(reverse('login:index'))

def success(request):
    return redirect(reverse('sheets:index'))


