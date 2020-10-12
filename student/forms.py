from .models import Student
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['is_student', 'user', 'is_attendence']


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'registration_number', 'is_attendence', 'is_student']
