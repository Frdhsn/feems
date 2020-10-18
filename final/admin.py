from django.contrib import admin
from .models import Student, Semister, Semister_Fee

# Register your models here.
admin.site.register(Student)
admin.site.register(Semister)
admin.site.register(Semister_Fee)
