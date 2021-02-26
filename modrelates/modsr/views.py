from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    hello = "Hello World"
    context = {'hello': hello}

    return render(request, "modsr/index.html", context)