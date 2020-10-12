from django.shortcuts import render, redirect
from .forms import StaffCreate
from django.contrib import messages

from student.models import Student


# Create your views here.


def staff(request):
    form = StaffCreate()

    if request.method == 'POST':
        form = StaffCreate(request.POST)

        if form.is_valid():
            dept = form.cleaned_data.get("department")
            role = form.cleaned_data.get("role")
            if role == "Teacher":
                return redirect('staff:all_student', dept=dept)
            elif role == "Hall Staff":
                return redirect('staff:hall_student')
            else:
                return redirect('staff:register_student')

    return render(request, 'staff/add_form.html', {'form': form})


def teachers_student(request, dept):
    students = Student.objects.filter(dept=dept)
    cont = {
        'students': students
    }
    return render(request, 'staff/teacher_student.html', cont)


def register_student(request):
    students = Student.objects.all()
    cont = {
        'students': students
    }
    return render(request, 'staff/register_student.html', cont)


def hall_student(request):
    students = Student.objects.all()
    cont = {
        'students': students
    }
    return render(request, 'staff/hall_student.html', cont)
