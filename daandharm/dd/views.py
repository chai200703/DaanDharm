from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm,DonationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group


def index(request):
    if request.user.is_authenticated:
        user = request.user
        full_name = user.get_full_name()    
        return render(request,'home.html',{'full_name':full_name})
    else:
        return render(request,'home.html')

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,"CONGRATULATION, You are Registered!")
            user = form.save()
            group = Group.objects.create(name = 'Author')
            user.groups.add(group)
    else:
        form=SignUpForm()
    return render(request,'registration.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request = request, data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                pwd = form.cleaned_data['password']
                user = authenticate(username=uname, password=pwd)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
            
        else:
            form = LoginForm()
       
        return render(request, 'login.html', {'form':form})
    else:
        return HttpResponseRedirect('/')
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')  

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation_type = form.cleaned_data['donation_type']
            full_address = form.cleaned_data['full_address']
            pickup_time = form.cleaned_data['pickup_time']
            
            return HttpResponseRedirect('/thank-you/')
    else:
        form = DonationForm()

    return render(request, 'donor.html', {'form': form})  