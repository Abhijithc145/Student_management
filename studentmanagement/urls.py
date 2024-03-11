from django.urls import path
from .views import StudentList,StudentDetails,StudentAttendentsDetails,AttendenceReport




urlpatterns = [
    path("students/", StudentList.as_view()),
    path("student/<uuid:pk>/", StudentDetails.as_view()),
    path("student/<uuid:pk>/attendence/", StudentAttendentsDetails.as_view()),
    path("students/attendence_report/", AttendenceReport.as_view()),
  
]
