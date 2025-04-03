from django.db import models

# Create your models here.

    
class Department(models.Model):
    name = models.CharField(max_length=255)
    head = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    
class Info(models.Model):
    name = models.CharField(max_length=255)
    emplopyee_id = models.PositiveIntegerField()
    college_name = models.CharField(max_length=255)
    date_of_joining = models.DateField()
    department = models.ForeignKey(Department,on_delete=models.PROTECT,null=True)
    
    
class Projects(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    

    
