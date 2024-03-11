from django.db import models
 
import uuid 

# Create your models here.

class Student(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    roll_number = models.CharField(max_length=3,null=False,blank=False)
    name = models.CharField(max_length=25,null=False,blank=False)
    mark = models.FloatField(null=True,blank=True,default=0)
    
    def __str__(self):
        return str(self.id)
    
class StudentAttendance(models.Model):
    class Leave_Types(models.TextChoices):
        HALF_DAY = "half_day", "Half day"
        FULL_DAY = "full_day", "Full day"
        None_type = "None", "None",

    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    date = models.DateField() 
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_present= models.BooleanField(default=True)
    leave_type = models.CharField(max_length=20, choices=Leave_Types.choices,default=Leave_Types.None_type,null=True)
    

    def __str__(self):
        return f"{self.student.name}"
        
    
    