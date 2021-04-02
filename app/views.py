from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return HttpResponse("heloooooooo")

def sam(request):
    return render(request,"sample.html")



