from django.shortcuts import render
import os
import psycopg2
from .models import Destination




# Create your views here..
def stud(request):
    return render(request,'Student.html')

def mult(request):
    var1 = int(request.GET['num1'])
    var2 = int(request.GET['num2'])
    summ = var1 + var2
    


    return render(request,'mul.html',{'result':summ})
