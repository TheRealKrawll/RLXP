from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h1>Landing Page</h1>")
    #render(request, "template_name", context{})

    #make a python dictionary
    my_context = {
        "hello_world": "CINS465 Hello World"

    }
    
    return render(request, "index.html", my_context)


