from django.shortcuts import render
import os
import psycopg2
from .models import Destination




# Create your views here..
def home(request):
    return render(request,'home.html')

def mult(request):
    dests = Destination.objects.all()


    return render(request,'mul.html',{'dests':dests})
