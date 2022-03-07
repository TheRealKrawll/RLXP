from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Duck
from .forms import DuckForm

# Create your views here.
def base(request):
    ducks = Duck.objects.all()

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
        "ducks": ducks

    }
    
    return render(request, "main/landing.html", my_context)


