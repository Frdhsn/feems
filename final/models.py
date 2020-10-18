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
    user = models.OneToOneField(
        User, related_name='student_user', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=20)
    registration_number = models.CharField(max_length=20)
    dept = models.CharField(max_length=100, choices=DEPT)
    batch = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Semister(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semister = models.CharField(max_length=10)
    hall = models.CharField(max_length=50)
    address = models.TextField()
    have_attendence = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.semister} semister form"


class Semister_Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semister = models.CharField(max_length=10)
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

    def __str__(self):
        return f"{self.student.name} {self.semister} Number Semister Fee"


class Staff(models.Model):
    ROLE = (
        ('Teacher', 'Teacher'),
        ('Register', 'Register')
    )

    dept = (
        ("IIT", "IIT"),
        ("CSE", "CSE"),
        ("LAW", 'LAW')
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    profession_id = models.CharField(max_length=100, null=True, blank=True)
    Role = models.CharField(max_length=100, blank=True,
                            null=True, choices=ROLE)
    department = models.CharField(
        max_length=100, null=True, blank=True, choices=dept)
    is_approved_by_register = models.BooleanField(default=True)

    def __str__(self):
        return self.name
