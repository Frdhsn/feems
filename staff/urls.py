from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "staff"
urlpatterns = [
    path("create/", views.staff, name='staff_create'),
    path('teacher_student/<str:dept>/',
         views.teachers_student, name='teacher_student'),
    path('register_student/', views.register_student, name='register_student'),
    path('hall_student/', views.hall_student, name='hall_student')


]
