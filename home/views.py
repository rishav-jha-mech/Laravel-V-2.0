from django.shortcuts import render, redirect
import time
from datetime import datetime
from home.models import Contact
from home.models import Blog
from django.contrib import messages
from hello import settings
from django.contrib.auth.decorators import login_required
from django.http import request
from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method== "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.now())
        contact.save()
        messages.success(request, 'Message Sent.')

    return render(request,"contact.html")

@login_required(redirect_field_name='/')  #this new thing will stop the us3er from accessing the write blog page and redirect thye user to login page
def writeablog(request):
    if request.method== "POST" and request.FILES['thumbnail']:
        name = request.POST.get('name')
        blogtitle = request.POST.get('blogtitle')
        blogsubtitle = request.POST.get('blogsubtitle')
        blogcontent = request.POST.get('blogcontent')
        thumbnail = request.FILES['thumbnail']
        fs = FileSystemStorage()
        filename = fs.save(thumbnail.name, thumbnail)
        blog = Blog(name=name,blogtitle=blogtitle,blogsubtitle=blogsubtitle,blogcontent=blogcontent,thumbnail=thumbnail,pub_date=datetime.now())
        blog.save()
        messages.success(request, 'Your Blog Is Posted Successfully')
    return render(request, "writeablog.html" )
    
def blogpost(request):
    myposts= Blog.objects.all()
    return render(request, 'blogpost.html',{'myposts':myposts})

def blog(request,id):
    post= Blog.objects.filter(post_id =id)[0]
    return render(request,'blog.html', {'post':post})

def handler404(request, exception):
    return render(request,'404.html')

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)

def admin(request):
    return redirect('tempo')
def accadmin(request):
    return redirect('tempo')

def tempo(request):
    return render(request,'404.html')

#AYUSH BHAIYA ASKED ME TO MAKE LOGIN LOGOUT SIGNUP  BY MYSELF :(

def handleSignup(request):
    if request.method == 'POST':
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        username= request.POST['username']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']
        #IF USER OVERIDES FRONT END AND GIVES EMPTY INPUT
        if fname=='':
            messages.error(request, "ENTER FIRST NAME PROPERLY")
        if lname=='':
            messages.error(request, "ENTER LAST NAME PROPERLY ")
        if email=='':
            messages.error(request, "ENTER EMAIL")
        if username=='':
            messages.error(request, "ENTER USERNAME")
        if pass1=='':
            messages.error(request, "ENTER PASSWORD")
        if pass2=='':
            messages.error(request, "CONFIRM ENTERED PASSWORD")
        
        #IF USER OVERIDES FRONT END AND GIVES EMPTY INPUT 
        
        if fname!='' and lname!='' and username!='' and pass1!='' and pass2!='' :
            
            if pass1 == pass2:
                user= User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=pass1)
                user.save()
                messages.info(request, "Your Account Has Been Successfully Created At Laravel. Please Log In To Continue")
                return redirect('login')
            else:
                messages.warning(request, "Please Check The Password You Have Entered")

        else:
            messages.warning(request, "ENTER THE FIELDS YOU DICKHEAD!")
        #messages.error(request, "HOGAYA ERROR")
        #messages.info(request, "HOGAYA INFO")
        #messages.warning(request, "HOGAYA WARNING")
        #messages.success(request, "HOGAYA SUCCESS")
    return render(request, "signup.html")


def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username= username, password= password)
        if user is not None:
            login(request, user)
            messages.info(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials! Please try again")
    return render(request,'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')