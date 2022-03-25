from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Duck, Room, Topic
from .forms import DuckForm, RoomForm

#queryset = Modelname.objects.all()
#.all() has many other methods (.get(), .filter(), .exclude(),...)
ducks = Duck.objects.all()


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
    }
    
    return render(request, "main/landing.html", my_context)


def duck(request, pk):
    #get the duck object by name
    duck = Duck.objects.get(name=pk)

    my_context = {
        'ducks': ducks,
        'duck': duck,
    }

    return render(request, 'main/duck.html', my_context)




##### TUTORIAL VIEWS #####


def mainroom(request):
    #in line if statement
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    #using double underscore is like saying topic.name
    #icontains will find any topic that contains what is in q
    # the i mean case insensitive
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    topics = Topic.objects.all()
    my_context = {
        "rooms": rooms,
        "topics": topics,
    }
    return render(request, 'main/mainroom.html', my_context)


def room(request, pk):
    #this is much better than the iteration version
    room = Room.objects.get(id=pk)
    """
    for rm in rooms:
        if rm.name == str(pk):
            room = rm
    """

    my_context = {"room": room}
    return render(request, 'main/room.html', my_context)

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        #print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainroom')

    my_context = {'form': form}
    return render(request, 'main/room_form.html', my_context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room) #This confuses me!

        if form.is_valid():
            form.save()
            #print("Worked")
            return redirect('mainroom')
            

    my_context = {'form': form}
    return render(request, 'main/room_form.html', my_context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete() #removes item from the database
        return redirect('mainroom')
    return render(request, 'main/delete.html', {'obj': room})



