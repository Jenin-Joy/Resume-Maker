from django.db import models
class tbl_Administrator(models.Model):
    Administrator_name=models.CharField(max_length=50);
    Administrator_email=models.CharField(max_length=50);
    Administrator_password=models.CharField(max_length=50);
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)
# class tbl_language(models.Model):
#     language=models.CharField(max_length=50)
class tbl_educationtype(models.Model):
    educationtype=models.CharField(max_length=50)    

class tbl_course(models.Model):
    educationtype=models.ForeignKey(tbl_educationtype,on_delete=models.CASCADE)
    course=models.CharField(max_length=50)