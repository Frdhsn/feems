from django.urls import path, include
from . import views

app_name = 'student'

urlpatterns = [
    path('student_form/', views.student_form, name='student_form'),
    path('verify/', views.verify, name='verify'),
    path('payment_form/', views.payment_form, name='payment_form'),
    path('payment_verify/', views.payment_verify, name='payment_verify'),
    path('update_student/', views.update_student, name='update_student')

]
