from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def index(request):
    return render(request,"products_app/index.html")

def checkout(request):
    return render(request,"products_app/checkout.html")

def shop(request):
    return render(request,"products_app/shop.html")

def contact(request):
    if(request.method=="POST"):
        n=request.POST.get("name")
        s=request.POST.get("subject")
        e=request.POST.get("email")
        m=request.POST.get("message")
        contactcls.objects.create(name=n,subject=s,email=e,message=m)
        return render(request,"products_app/message.html")
    return render(request,"products_app/contact-us.html")

def about(request):
    return render(request,"products_app/about-us.html")

def log(request):
    if(request.method=="POST"):
        u=request.POST.get("username")
        p=request.POST.get("password")
        user=authenticate(request,username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect("/cart")
        else:
            return redirect("/error")


    return render(request,"products_app/login.html")

def sign(request):
    if request.method=="POST":
        status=False
        context={"errors":[]}
        n=request.POST.get("name")
        l=request.POST.get("lname")
        e=request.POST.get("email")
        u=request.POST.get("username")
        p=request.POST.get("password")
        rp=request.POST.get("rpassword")
        if len(p)<6:
            status=True
            context["errors"].append("password must be 6 characters")
        if p!=rp:
            status=True
            context["errors"].append("re_password is not match")

        if(status==False):    
            User.objects.create(first_name=n,last_name=l,email=e,username=u,password=p)
            return redirect("/success") 
        else:
            return render(request,"products_app/sign-up.html",context=context)
        
    return render(request,"products_app/sign-up.html")
    
def sc(request):
    return render(request,"products_app/success.html")    

def cart(request):
    if request.user.is_authenticated:
       return render(request,"products_app/cart.html")
    else:
        return redirect("/login")

def lout(request):
    logout(request)
    return redirect("/")

def error(request):
    return render(request,"products_app/error.html")