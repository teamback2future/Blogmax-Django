from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import RegisterForm, LoginForm, UserUpdateForm, UserProfileUpdate
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! You are now able to login")

            return redirect("users:login")
    else:
        form = RegisterForm()
   
    return render(request,"users/register.html",{'form':form})

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password=password)

        if user is None:
            messages.warning(request,"Username or password is wrong!")
            return render(request,"users/login.html",context)
        
        messages.success(request, f"Welcome, {username}")
        login(request, user)
        return redirect("blog-home")
    
    return render(request,"users/login.html",context)

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        i_form = UserProfileUpdate(request.POST, request.FILES ,instance=request.user.profile)
        if u_form.is_valid() and i_form.is_valid():
            u_form.save()
            i_form.save()
            messages.success(request, f"Your account has been updated")

            return redirect("users:profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        i_form = UserProfileUpdate(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'i_form':i_form
    }
    return render(request,"users/profile.html",context)
