from random import randint
from rest_framework import serializers
from datetime import datetime, timedelta, date, timezone

from home.models import StudentInformation, User


class HomePageSerializer(serializers.Serializer):
    o_pos = serializers.SerializerMethodField()
    o_neg = serializers.SerializerMethodField()
    a_pos = serializers.SerializerMethodField()
    a_neg = serializers.SerializerMethodField()
    b_pos = serializers.SerializerMethodField()
    b_neg = serializers.SerializerMethodField()
    ab_pos = serializers.SerializerMethodField()
    ab_neg = serializers.SerializerMethodField()
    total_donated_students = serializers.SerializerMethodField()
    
    def get_o_pos(self, obj):
        return StudentInformation.objects.filter(blood_group='O+ve').exclude(year_out__lte=date.today().year).count()
    
    def get_o_neg(self, obj):
        return StudentInformation.objects.filter(blood_group='O-ve').exclude(year_out__lte=date.today().year).count()
    
    def get_a_pos(self, obj):
        return StudentInformation.objects.filter(blood_group='A+ve').exclude(year_out__lte=date.today().year).count()
    
    def get_a_neg(self, obj):
        return StudentInformation.objects.filter(blood_group='A-ve').exclude(year_out__lte=date.today().year).count()
    
    def get_b_pos(self, obj):
        return StudentInformation.objects.filter(blood_group='B+ve').exclude(year_out__lte=date.today().year).count()
    
    def get_b_neg(self, obj):
        return StudentInformation.objects.filter(blood_group='B-ve').exclude(year_out__lte=date.today().year).count()
    
    def get_ab_pos(self, obj):
        return StudentInformation.objects.filter(blood_group='AB+ve').exclude(year_out__lte=date.today().year).count()
    
    def get_ab_neg(self, obj):
        return StudentInformation.objects.filter(blood_group='AB-ve').exclude(year_out__lte=date.today().year).count()
    
    def get_total_donated_students(self, instance):
        student = StudentInformation.objects.all().exclude(year_out__lte=date.today().year)
        lis = []
        for x in student:
            if x.eligible:
                lis.append(1)
        return len(lis)


class SpecificStudentSerializer(serializers.ModelSerializer):
    day_left = serializers.SerializerMethodField()
    class Meta:
        model = StudentInformation
        fields = ['student_id', 'register_no', 'student_name', 'department', 'phone_no', 'place', 'dob', 'blood_group', 'eligible', 'last_donated_date', 'day_left']
    
    def get_day_left(self, instance):
        if instance.last_donated_date is not None:
            days_left = (date.today() - instance.last_donated_date).days
            if days_left < 84:
                return days_left
            else:
                days_left = 0
                return days_left
        else:
            days_left = 0
            return days_left


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInformation
        fields = ['student_id', 'student_name', 'eligible']


class YearOutStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInformation
        fields = ['student_id', 'student_name']


class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    

class OtpVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.IntegerField()
        

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
