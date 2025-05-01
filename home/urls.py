from django.urls import path

from home.views.student import (
    SpecificStudentRetrieveView,
    HomePageView,
    SpecificBloodView,
    ForgetPasswordView,
    OtpVerifyView,
    ResetPasswordView,
    YearOutStudentView,
    DeleteYearOutStudentView,)
from home.views.addstudentview import addStudent

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', addStudent, name='add-student'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/forget-password/', ForgetPasswordView.as_view(), name='forget_password'),
    path('api/otp-verify/', OtpVerifyView.as_view(), name='otp_verify'),
    path('api/reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('home/', HomePageView.as_view(), name="home"),
    path('blood/<pk>/', SpecificBloodView.as_view(), name="home"),
    path('specific-student-details/<pk>/', SpecificStudentRetrieveView.as_view()),
    path('year-out-students/', YearOutStudentView.as_view(), name='year_out_students'),
    path('specific-year-out-student/<pk>/', DeleteYearOutStudentView.as_view(), name='detail_year_out_student'),
]

# urlpatterns += 