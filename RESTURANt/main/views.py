from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Contact
# from .models import Index
from datetime import datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.
date=datetime.now().year

def index(request):
   
    
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        IN=Contact(name=name,email=email,phone=phone,message=message)
        IN.save()

        subject='contact form'
        message=render_to_string('message.html',{'name':name})
        from_email='adhikarynita659@gmail.com'
        recipient_list=[email]
        send_mail(subject,message,from_email,recipient_list,fail_silently=False)
        messages.success(request,'successfully send')
    return render(request,'index.html',{'date':date})

def about(request):
    
    return render(request,'about.html',{'date':date})
  

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        con=Contact(name=name,email=email,phone=phone,message=message)
        con.save()

        subject='contact form'
        message=render_to_string('message.html',{'name':name})
        from_email='adhikarynita659@gmail.com'
        recipient_list=[email]
        send_mail(subject,message,from_email,recipient_list,fail_silently=False)
        messages.success(request,'successfully send')
    return render(request,'contact.html')

def menu(request):
   
    
    return render(request,'menu.html',{'date':date})
  

def services(request):
  
    return render(request,'services.html',{'date':date})
    
    

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is already valid')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is already valid')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,'successfully register')
                return redirect('log_in')
            

        else:
            messages.error(request,'password is not valid')
            return redirect('register')

    return render(request,'auth/register.html')

def log_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        if not User.objects.filter(username=username).exists():
            messages.info(request,'username doesnot exists')
            return redirect('log_in')

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'invalid keyword!')
            return redirect('log_in')


    return render(request,'auth/login.html')
def log_out(request):
    logout(request)
    return redirect('log_in')