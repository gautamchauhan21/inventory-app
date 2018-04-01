from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.views import generic
from django.http import HttpResponse
from myapp.models import Inventory
def home(request):
    names = Inventory.objects.all()
    return render(request, 'myapp/home.html', { "names": names})

def added(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    item.stocks_left += 1
    item.save()
    names = Inventory.objects.all()
    return render(request, 'myapp/added.html', { "names": names})

def subtracted(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    item.stocks_left -= 1
    item.save()
    names = Inventory.objects.all()
    return render(request, 'myapp/subtracted.html', { "names": names})
