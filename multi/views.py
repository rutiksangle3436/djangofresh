from django.shortcuts import render
import os
import psycopg2

DATABASE_URL = os.environ['ec2-52-70-15-120.compute-1.amazonaws.com:5432/dcemse6mcjhbg']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
# Create your views here..
def home(request):
    return render(request,'home.html')

def mult(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 * val2

    return render(request,'mul.html',{'result':res})
