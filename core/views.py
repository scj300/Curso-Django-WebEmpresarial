from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Home</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")

def services(request):
    return HttpResponse("<h1>Services</h1>")

def store(request):
    return HttpResponse("<h1>Visit Us</h1>")

def contact(request):
    return HttpResponse("<h1>Contact</h1>")