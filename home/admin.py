from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import StudentInformation, User


admin.site.register(User, UserAdmin)


class CustomStudentInfo(admin.ModelAdmin):
    list_display = ('student_id', 'student_name', 'register_no', 'place', 'blood_group', 'eligible', 'year_out_student', 'last_donated_date')

admin.site.register(StudentInformation, CustomStudentInfo)



