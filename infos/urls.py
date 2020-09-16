from django.contrib import admin
from django.urls import path
from infos.views import homepage, me, contact

urlpatterns = [
    path('', homepage),
    path('me', me),
    path('contact', contact),
]