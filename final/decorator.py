from django.shortcuts import render, redirect
from .models import Student


def exists_student(view_func):
    def wrapper_func(request, *args, **kwargs):
        if Student.objects.filter(user=request.user):
            return redirect('final:semister_form')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def unauthorizeduser(called_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('final:homepage')
        else:
            return called_func(request, *args, **kwargs)
    return wrapper
