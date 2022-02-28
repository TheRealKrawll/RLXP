from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request): #look them up!!!! wtf are you
    return HttpResponse("<h1>Home Page</h1>") #string of html code

def contact_view(request):
    return HttpResponse("<h1>Contact Page</h1>")