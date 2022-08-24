from django.shortcuts import render
from .models import Familiares


def home(request):
    return render(request, 'home.html', context={})


def crear_familia(request):
    familiar1 = Familiares.objects.create(name="Javier", age="60", date="1962-11-12")
    familiar2 = Familiares.objects.create(name="Cristina", age="68", date="1954-12-08")
    familiar3 = Familiares.objects.create(name="Ariel", age="31", date="1991-08-20")
    context = {
        'familiar1': familiar1,
        'familiar2': familiar2,
        'familiar3': familiar3,
    }
    return render(request, 'home.html', context)