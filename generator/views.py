from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    passWord = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    len = int(request.GET.get('length', 12))

    if request.GET.get('upper'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('char'):
        characters.extend(list('!@#$%^&*'))

    for i in range(len):
        passWord += random.choice(characters)

    return render(request, 'generator/password.html', {"password": passWord})



