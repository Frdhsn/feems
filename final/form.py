from .models import Student, Semister, Staff
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'roll', 'registration_number',
                  'dept', 'batch', 'phone_number')


class SemisterForm(forms.ModelForm):
    class Meta:
        model = Semister
        fields = '__all__'
        exclude = ['student', 'have_attendence']


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        exclude = ['is_approved_by_register']


class UpdateStudentByRegister(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['is_student']


class UpdateStudentByTeacher(forms.ModelForm):
    class Meta:
        model = Semister
        fields = ['have_attendence']
