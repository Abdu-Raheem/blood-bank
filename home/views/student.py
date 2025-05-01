from random import randint
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import date, datetime, timedelta
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password


from home.models import StudentInformation, User
from home.serializers.student import (
    SpecificStudentSerializer,
    ForgetPasswordSerializer,
    HomePageSerializer,
    StudentListSerializer,
    OtpVerifySerializer,
    ResetPasswordSerializer,
    YearOutStudentSerializer,)
    

class ForgetPasswordView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = ForgetPasswordSerializer(data=request.data, many=False)
        if serializer.is_valid():
            if not User.objects.filter(email=request.data["email"]).exists():
                return Response({"message": 'Email does not exists'}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(email=request.data["email"])
            user.otp = randint(1000, 9999)
            user.otp_expiry = datetime.now() + timedelta(minutes=5)
            user.save(update_fields=['otp', 'otp_expiry'])
            subject = 'Your OTP for Jeevana App'
            message = f'Hello {user.first_name}, \n\nYour One-Time Password (OTP) for accessing the Jeevana app is: {user.otp} \n\nIf you didnt request this OTP, please ignore this email \n\nThank you for using Jeevana App.\nBest regards,\nJeevana App Team'
            email_from = settings.EMAIL_HOST
            send_mail(subject, message, email_from, [user.email])
            return Response({"message": "Otp sent successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class OtpVerifyView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = OtpVerifySerializer(data=request.data, many=False)
        if serializer.is_valid():
            user = User.objects.get(email=request.data['email'])
            if user.otp == int(request.data["otp"]):
                return Response({"message": "Correct Otp"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Wrong Otp"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    permission_classes = [AllowAny]
    def put(self, request):
        serializer = ResetPasswordSerializer(data=request.data, many=False)
        if serializer.is_valid():
            user = User.objects.get(email=request.data['email'])
            user.password = make_password(request.data['password'])
            user.save()
            return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomePageView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        queryset = StudentInformation.objects.filter(year_out__lte=date.today().year)
        serializer = HomePageSerializer(queryset, many=False, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class SpecificBloodView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = StudentListSerializer
    def get_queryset(self):
        blood = self.kwargs["pk"]
        return StudentInformation.objects.filter(blood_group=blood).exclude(year_out__lte=date.today().year)
    

class SpecificStudentRetrieveView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        queryset = StudentInformation.objects.get(student_id=pk)
        serializer = SpecificStudentSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        queryset = StudentInformation.objects.get(student_id=pk)
        serializer = SpecificStudentSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class YearOutStudentView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        queryset = StudentInformation.objects.filter(year_out__lte=date.today().year)
        serializer = YearOutStudentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     
     
class DeleteYearOutStudentView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk, format=None):
        queryset = StudentInformation.objects.get(student_id=pk)
        serializer = SpecificStudentSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, pk, format=None):
        queryset = StudentInformation.objects.get(student_id=pk)
        queryset.delete()
        return Response({"message": "Deleted Successfully"}, status=status.HTTP_200_OK)