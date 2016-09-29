from django.shortcuts import render, redirect
from ..loginreg.models import User
from .models import Character
from .forms import CharacterForm
from django.core.urlresolvers import reverse
from django.contrib import messages

# Create your views here.
def index(request):
    u = User.get(id=request.session['id'])
    c = Character.filter(user=u)
    context = {
        'user': u,
        'characters': c
    }
    return render(request, 'sheets/index.html', context)

def add(request):
    return render(request, 'sheets/add.html')

def create(request):
    if request.method == 'POST':
        bound_form = CharacterForm(request.POST)
        if bound_form.is_valid():
            c = Character.manager.create(bound_form)
            # TODO: redirect to show page for Character
            return redirect(reverse('sheets:index'))
        else:
            for e in bound_form.errors:
                messages.error(request, e)
    return redirect(reverse('sheets:add'))

def show(request):
    
