from django.db import models
class tbl_UserRegistration(models.Model):
    UserRegistration_photo=models.FileField(upload_to="Assets/User/")
    UserRegistration_name=models.CharField(max_length=50)
    UserRegistration_email=models.CharField(max_length=50)
    UserRegistration_password=models.CharField(max_length=50)
    UserRegistration_contact=models.CharField(max_length=50)
