from django.shortcuts import render
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request,'Login.html')
    else:
        email = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"logged.html",{'us':user})
        else:
            return render(request,'Login.html',{'status':"Incorrect Email or Password!"})    
