from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    DEPT = (
        ("IIT", "IIT"),
        ("CSE", "CSE"),
        ("Mathmatics", "Mathmatics"),
        ("Statistics", "Statistics")
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    roll = models.CharField(max_length=100, null=True)
    registration_number = models.CharField(max_length=100, null=True)
    semister = models.CharField(max_length=10, null=True)
    dept = models.CharField(max_length=100,
                            null=True, choices=DEPT)
    batch = models.CharField(max_length=100,  null=True)
    phone_number = models.CharField(max_length=100,  null=True)
    is_student = models.BooleanField(default=False)
    is_attendence = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Student_Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    admission_fee = models.FloatField(null=True)
    session_charge = models.FloatField(null=True)
    exam_fee = models.FloatField(null=True)
    hall_fee = models.FloatField(null=True)
    library_fee = models.FloatField(null=True)
    transport_fee = models.FloatField(null=True)
    medical_fee = models.FloatField(null=True)
    bank_sleep = models.BooleanField(default=True)
    is_hall_verify = models.BooleanField(default=False)
    is_register_verify = models.BooleanField(default=False)
