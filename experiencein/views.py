# editando o arquivo experiencein/perfis/views.py

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Bem-vindo ao Experiencein')