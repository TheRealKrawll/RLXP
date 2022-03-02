from django.shortcuts import render

# Create your views here.
def base(request):
    my_context = {
        "hello_world": "CINS465 Hello World"
    }
    
    return render(request, "landing.html", my_context)