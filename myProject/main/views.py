from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

# Create your views here.
def base(request):

    if request.method == 'POST':
        name_form = NameForm(request.POST)
        if name_form.is_valid():
            HttpResponseRedirect("Thanks")
    else:
        name_form = NameForm


    my_context = {
        "hello_world": "CINS465 Hello World",
        "another": "another",
        "name_form" : name_form,

    }
    
    return render(request, "main/landing.html", my_context)


#Show the results of a form
def name_view(request):
    return render(request, "main/index.html", {})
