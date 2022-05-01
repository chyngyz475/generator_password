from xml.dom.pulldom import CHARACTERS
from django.shortcuts import render
from django.http import HttpResponse
import random

from numpy import character

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'xsyusp'})

def password(request):
    
    characters = list('abcdefghisjlmopqrstuvwzyz')
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    
    length = int(request.GET.get('length',14))
    
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password':thepassword})

def description(request):
    return render(request, 'generator/description.html')