from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import Customer
from django.contrib import messages


# Create your views here.
def show_account(request):
    context={}
    if request.POST and 'Register_btn' in request.POST:
        context['Register_btn']=True

        try:    
            username=request.POST.get('Username')
            password=request.POST.get('Password')
            address=request.POST.get('Address')
            mobile=request.POST.get('Mobile')
            email=request.POST.get('Email')
            # create user account
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            #create custmer account
            customer=Customer.objects.create(
                user=user,
                phone=mobile,
                address=address
            )
            success_message="Your account has been successfully created."
            messages.success(request,success_message)
        except Exception as e:
            error_message="The username already exists try again with new username"
            messages.error(request,error_message)
    if request.POST and 'login_btn' in request.POST:
        context['Register_btn']=False

        username=request.POST.get('Username')
        password=request.POST.get('Password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home_page')
        else:
            error_message="invalid username "
            messages.error(request,error_message)

    return render(request,'account.html',context)

def sign_out(request):
    logout(request)
    return redirect('home_page')


