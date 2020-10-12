from django.db import models

# Create your models here.


class Staff(models.Model):
    ROLE = (
        ('Teacher', 'Teacher'),
        ("Hall Staff", 'Hall Staff'),
        ('Register', 'Register')
    )

    dept = (
        ("IIT", "IIT"),
        ("CSE", "CSE"),
        ("LAW", 'LAW')
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    Role = models.CharField(max_length=100, blank=True,
                            null=True, choices=ROLE)
    department = models.CharField(
        max_length=100, null=True, blank=True, choices=dept)
    hall_name = models.CharField(max_length=100, null=True, blank=True)
    is_approved_by_register = models.BooleanField(default=True)

    def __str__(self):
        return self.name
