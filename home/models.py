from typing import Iterable, Optional
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from random import randint
from django.utils import timezone
from datetime import timedelta, date



class User(AbstractUser):
    otp = models.IntegerField(null=True, blank=True)
    otp_expiry = models.DateTimeField(blank=True, null=True)
    

BLOOD_GROUP = (
    ('A+ve', 'A+ve'),
    ('A-ve', 'A-ve'),
    ('B+ve', 'B+ve'),
    ('B-ve', 'B-ve'),
    ('AB+ve', 'AB+ve'),
    ('AB-ve', 'AB-ve'),
    ('O+ve', 'O+ve'),
    ('O-ve', 'O-ve')
)

DEPARTMENT = (
    ('CS', 'CS'),
    ('EC', 'EC'),
    ('EE', 'EE'),
    ('IT', 'IT'),
    ('CE', 'CE'),
    ('ME', 'ME')
)


class StudentInformation(models.Model):
    student_id = models.BigAutoField(primary_key=True, unique=True)
    register_no = models.CharField(max_length=20, unique=True)
    student_name = models.CharField(max_length=150)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$')
    phone_no = models.CharField(
        validators=[phone_regex], max_length=10, blank=False)
    place = models.CharField(max_length=150)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP, default='NULL')
    dob = models.DateField()
    department = models.CharField(max_length=10, choices=DEPARTMENT)
    last_donated_date = models.DateField(null=True, blank=True)
    year_out = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and not self.year_out:
            self.year_out = int(self.register_no[-7:-5:1]) + 2000 + 4
        return super(StudentInformation, self).save(*args, **kwargs)

    @property
    def eligible(self):
        if self.last_donated_date is not None:
            if self.last_donated_date + timedelta(days=84) <= date.today():
                return True
            return False
        else:
            return True
        
    @property
    def year_out_student(self):
        if self.year_out <= date.today().year:
            return True
        else:
            return False

    class Meta:
        db_table = "StudentInformation"

    def __str__(self):
        return str(self.student_id) + " " + self.student_name + " " + self.place + " " + str(self.eligible) + " " + str(self.year_out_student)

    


    
