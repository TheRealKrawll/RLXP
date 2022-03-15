from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Duck
from .forms import DuckForm

ducks = Duck.objects.all()

rooms = [
    {'id': 1, 'name': 'room 1'},
    {'id': 2, 'name': 'room 2'},
    {'id': 3, 'name': 'room 3'},
]

# Create your views here.
def base(request):
    if request.method == 'POST':
        name_form = DuckForm(request.POST)
        if name_form.is_valid():
            name_form.save()
            name_form = DuckForm()            
    else:
        name_form = DuckForm()


    my_context = {
        "hello_world": "CINS465 Hello World",
        "name_form" : name_form,
        "ducks": ducks,
        "rooms": rooms,

    }
    
    return render(request, "main/landing.html", my_context)


def mainroom(request):
    my_context = {
        "rooms": rooms,
    }
    return render(request, 'main/room.html', my_context)

def room(request, pk):
    room = None
    for rm in rooms:
        if rm['id'] == int(pk):
            room = rm

    my_context = {"room": room}
    return render(request, 'main/room.html', my_context)


def duck(request, pk):
    duck = None

    #get the duck object by name
    for dk in ducks:
        if dk.name == str(pk):
            duck = dk

    my_context = {
        'ducks': ducks,
        'duck': duck,
    }

    return render(request, 'main/duck.html', my_context)
