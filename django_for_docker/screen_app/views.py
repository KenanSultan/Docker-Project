from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    a = HttpResponse('Kenan Sultan')

    return a
