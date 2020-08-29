from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render (request,'home/home.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<5:
            messages.error(request,'Please fill the form correctly')
        else: 
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,'Your form is submitted sucessfully')
    return render(request,'home/contact.html')

def community(request):
    return render(request,'home/community.html')

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Sucessfully logged in")
            return render(request,'home/home.html')
        else:
            messages.error(request,"Innvalid Username or password")
            return redirect('home')
    return HttpResponse('404 - Not Found')

def handlelogout(request):
    logout(request)
    messages.success(request,"Sucessfully logged out")
    return render(request,'home/home.html')

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        fname = request.POST['fname']
        lname = request.POST['lname'] 
        
        #Username should be alphanumeric
        if not username.isalnum():
            messages.error(request,'Username should contain only alphanumeric characters')
            return render(request,'home/home.html')
        # Password should match
        if pass1 != pass2:
            messages.error(request,'Password did not match ')
            return redirect('home')

        myuser = User.objects.create_user(username,email,pass1)  
        myuser.first_name = fname  
        myuser.last_name = lname  
        myuser.save()
        messages.success(request,"Your account has been created sucessfully")
        return render(request,'home/home.html')
    else:
        return HttpResponse('404 -Not Found')

def search(request):
    return render(request,'home/search.html')

