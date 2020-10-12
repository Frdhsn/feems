from django.shortcuts import render, redirect
from .forms import StudentForm, UpdateStudentForm
from django.contrib import messages
from .models import Student_Fee

from .models import Student

# Create your views here.


def student_form(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.info(
                request, f"Your Student Verify form submitted Successfully")
            return redirect("student:verify")

    cont = {
        'form': form
    }
    return render(request, 'student/student_form.html', cont)


def verify(request):
    student = Student.objects.filter(user=request.user).last()

    is_student = student.is_student
    is_attendence = student.is_attendence
    permission = False
    if is_attendence and is_student:
        permission = True

    cont = {
        'permission': permission
    }
    return render(request, 'student/verify.html', cont)


def payment_form(request):
    student = Student.objects.filter(user=request.user).last()
    if request.method == "POST":
        student = student
        admission_fee = request.POST.get("admission_fee")
        session_charge = request.POST.get("session_charge")
        exam_fee = request.POST.get("exam_fee")
        hall_fee = request.POST.get("hall_fee")
        library_fee = request.POST.get("library_fee")
        transport_fee = request.POST.get("transport_fee")
        medical_fee = request.POST.get("medical_fee")

        form = Student_Fee(student=student,
                           admission_fee=admission_fee,
                           session_charge=session_charge,
                           exam_fee=exam_fee,
                           hall_fee=hall_fee,
                           library_fee=library_fee,
                           transport_fee=transport_fee,
                           medical_fee=medical_fee)
        form.save()
        messages.info(request, f"Your Payment Is completed")
        return redirect("student:payment_verify")

    return render(request, 'student/payment_form.html')


def payment_verify(request):
    student = Student.objects.filter(user=request.user).last()
    print("student", student)

    student_fee = Student_Fee.objects.filter(student=student).last()
    print(student_fee)

    is_hall_verify = student_fee.is_hall_verify
    is_register_verify = student_fee.is_register_verify

    get_admit_card = False
    if is_hall_verify and is_register_verify:
        get_admit_card = True

    cont = {
        'get_admit_card': get_admit_card
    }

    return render(request, 'student/hall_reg_verify.html', cont)


def update_student(request):
    student = Student.objects.filter(user=request.user).last()
    form = UpdateStudentForm(instance=student)

    if request.method == "POST":
        form = UpdateStudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.info(request, f'Student Info Updated')
            return redirect('user:home')

    return render(request, 'student/student_form.html', {'form': form})
