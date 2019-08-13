from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    respu ="<ul>"
    respu= respu +"<li>#1</li>"
    respu= respu +"<li>#1</li>"
    respu= respu +"</ul>"
    return HttpResponse(respu)

def nuevococinero(request):
    return HttpResponse("<p>esta es la pagina de cocinero</p>")

def consultarpedido(request):
    return HttpResponse("OMG")

def redes(request):
    return HttpResponse("<h1>:v = pacman</h1>") 