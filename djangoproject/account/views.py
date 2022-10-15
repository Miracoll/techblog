from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UpdateForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import User

# Create your views here.

def registeruser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')
            return redirect('register')
    else:
        form = UserRegistrationForm()
    context = {'display':form}
    return render(request, 'account/register.html', context)

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request,'username does not exist')
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'username/password is incorrect')
            return redirect('login')
    return render(request, 'account/login.html')

def profile(request):
    return render(request, 'account/profile.html')

# def updateprofile(request, pk):
#     getid = User.objects.get(username=request.user.username).id
#     print(getid)
#     profile = User.objects.get(id=getid)
#     form = UpdateForm(instance=profile)
#     if request.method == 'POST':
#         form = UpdateForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated successfully')
#             return redirect('home')
#     return render(request, 'account/updateprofile.html', {'form':form})