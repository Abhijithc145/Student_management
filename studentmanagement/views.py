
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student,StudentAttendance
from .serializers import StudentSerializer,AttentenceSerializer

from django.core.paginator import Paginator
import datetime


class StudentList(APIView):
    def get(self,request):
        
        stuent_list=Student.objects.all()
        student_serilizer=StudentSerializer(stuent_list,many=True)
        return Response(
  
        {
            "status": 200,
            "message": "Student List",
            "data": student_serilizer.data,
            
        },
        status=status.HTTP_200_OK,
    )
    def post(self,request):
        try:
            Student.objects.create(name=request.data['name'],roll_number=str(request.data['roll_number']))
            return Response({"Message": "New record created"})
        except Exception as Error:
            return Response({"message":str(Error)})
        
class StudentDetails(APIView):
    def get(self,request,pk):
        student_detail=Student.objects.get(id=pk)
        student_serilizer=StudentSerializer(student_detail).data
        return Response(student_serilizer)
    
    def put(self,request,pk):
        try:
            if request.data.get('mark',None)==None:
                return Response({"Messge":"Mark filed not entered"})
            
            student_detail=Student.objects.get(id=pk)
            student_detail.mark=float(request.data['mark'])
            student_detail.save()
            return Response({"Message": "Record updated"})
        except Exception as Error:
            return Response({"message":str(Error)})
            
   
class StudentAttendentsDetails(APIView):
    def get(self,request,pk):
        try:
            student_attentence= StudentAttendance.objects.filter(student_id=pk)
            student_attentence_serilizer= AttentenceSerializer(student_attentence,many=True)
            return Response({"message ":student_attentence_serilizer.data},)
        except Exception as Error:
            return Response({"message":str(Error)})
    
    def post(self,request,pk):
        try:
            # Student.objects.create(name=request.data['name'],roll_number=str(request.data['roll_number']))
            StudentAttendance.objects.create(student_id=pk,is_present=request.data['is_present'],leave_type=request.data.get('leave_type',None),date=request.data['date'])
            
            
            return Response({"Message": "New record created"})
            
            
        except Exception as Error:
            return Response({"message":str(Error)})
        
        
        
class AttendenceReport(APIView):
    def get(self,request):
        try:
            students= Student.objects.all()
            student_attendece=[]
            attendence_details=StudentAttendance.objects.all()
            for student in students:
                student_attendence_present= attendence_details.filter(student_id=student.id,is_present=True).count()
                student_attendence_notpresent_fullday= attendence_details.filter(student_id=student.id,is_present=False,leave_type="full_day").count()
                
                student_attendence_notpresent_halfday= attendence_details.filter(student_id=student.id,is_present=False,leave_type="half_day").count()
                total_attendence=student_attendence_present+student_attendence_notpresent_fullday+(student_attendence_notpresent_halfday//2)
                attendence_percentage=(student_attendence_present/total_attendence)*100
                
                student_attendece.append({
                    "student_name":student.name,
                    "total_leave":total_attendence-student_attendence_present,
                    "total_persentate":total_attendence,
                    "total_attendence_perentage":attendence_percentage
                })
                
          
            return Response({"message":str(student_attendece)})
        except Exception as Error:
            return Response({"message":str(Error)})
            