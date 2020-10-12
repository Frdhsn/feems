from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    return render(request, 'user/home.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('user:home')
    else:
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get("username")
                messages.success(request, f"Signup Completed By {username}")
                return redirect("user:signin")

        cont = {
            'form': form
        }
        return render(request, 'user/signup.html', cont)
