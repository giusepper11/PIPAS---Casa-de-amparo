from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tempIndex(request):
    return HttpResponse('<h1>Em breve !!!</h1>')