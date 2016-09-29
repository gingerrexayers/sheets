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
            c = Character.manager.new_character(bound_form.cleaned_data)
            return redirect(reverse('sheets:show', kwargs={'id':c['id']}))
        else:
            for e in bound_form.errors:
                messages.error(request, e)
    return redirect(reverse('sheets:add'))

def show(request, id):
    c = Character.get(id=id)
    form = CharacterForm(c)
    context = {
        'character': c,
        'form': form
    }
    return render(request, 'sheets/show.html', context)

def update(request, id):
    if request.method == 'POST':
        bound_form = CharacterForm(id, request.POST)
        if bound_form.is_valid():
            Character.manager.update_character(bound_form)
        else:
            for e in bound_form.errors:
                messages.error(request, e)
    return redirect(reverse('sheets:show', kwargs={'id':id}))

def delete(request, id):
    c = Character.get(id=id)
    c.delete()
    return redirect(reverse('sheets:index'))
