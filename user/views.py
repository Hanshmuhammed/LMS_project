from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . models import User

# Create your views here.
def user_page(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')

            if password1 != password2:
                messages.error(request, "Passwords do not match!")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered!")
            else:
                user = User.objects.create_user(username=username, 
                                                email=email, 
                                                password=password1)
                success_message='registed succesfully'
                messages.success(request,success_message)
        except Exception as e:
            error_message='duplicate name or invalid inputs'
            messages.error(request,error_message)

    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    
        if user is not None:  # Authenticate successful
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')
        else:  # Authentication failed
            messages.error(request, "Invalid credentials!")
      

    return render(request,'user.html',context)