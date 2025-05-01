from django.forms import ModelForm
from django import forms

from home.models import StudentInformation


class AddStudentForm(ModelForm):
    class Meta:
        model = StudentInformation
        fields = ['register_no', 'student_name', 'phone_no', 'place', 'blood_group', 'dob', 'department', 'last_donated_date']
