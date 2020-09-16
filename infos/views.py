from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def homepage(request):
    t = loader.get_template("infos/homepage.html")
    c = {"title": "home"}
    return HttpResponse(t.render(c))

def me(request):
    t = loader.get_template("infos/me.html")
    c = {"title": "About me"}
    return HttpResponse(t.render(c))

def contact(request):
    t = loader.get_template("infos/contact.html")
    c = {"title": "Contact"}
    return HttpResponse(t.render(c))