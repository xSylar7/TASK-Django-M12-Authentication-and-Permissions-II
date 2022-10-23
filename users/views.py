from multiprocessing import context
from django.shortcuts import render, redirect
from users.forms import UserSignupForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def user_sign_up(request):
    form = UserSignupForm
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("home")
    context = {
        'form': form,
    }
    return render(request, 'user_signup.html', context)


def user_logout(request):
    logout(request)
    return redirect("home")


def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect("home")
    context = {
        'form': form,
    }
    return render(request, "user_login.html", context)
