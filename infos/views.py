from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def homepage(request):
    c = {"title": "home"}
    return render(
        request=request,
        template_name="infos/homepage.html",
        context=c
    )


def me(request):
    c = {"title": "About me"}
    return render(
        request=request,
        template_name="infos/me.html",
        context=c
    )


def contact(request):
    c = {"title": "Contact"}
    return render(
        request=request,
        template_name="infos/contact.html",
        context=c
    )
