from django.db import models
from Guest.models import *
from Administrator.models import *
class tbl_Education(models.Model):
    Education_Institution=models.CharField(max_length=50)
    Education_Course=models.ForeignKey(tbl_course,on_delete=models.CASCADE)
    Education_StartDate=models.CharField(max_length=50)
    Education_EndDate=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_UserRegistration,on_delete=models.CASCADE)
class tbl_about(models.Model):
    about_name=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_UserRegistration,on_delete=models.CASCADE)
class tbl_Experience(models.Model):
    Experience_Jobtitle=models.CharField(max_length=50)
    Experience_Companyname=models.CharField(max_length=50)
    Experience_Experience=models.CharField(max_length=50)
    Experience_Startdate=models.CharField(max_length=50)    
    Experience_Enddate=models.CharField(max_length=50)
    Experience_Description=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_UserRegistration,on_delete=models.CASCADE)
class tbl_Project(models.Model):
    Project_Name=models.CharField(max_length=50)
    Project_Details=models.CharField(max_length=50)
    Project_Link=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_UserRegistration,on_delete=models.CASCADE) 
class tbl_skill(models.Model):
    skill_name=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_UserRegistration,on_delete=models.CASCADE)
class tbl_language(models.Model):
    language_name=models.CharField(max_length=50)
    language_level=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_UserRegistration,on_delete=models.CASCADE)
class tbl_hobbies(models.Model):
    hobbies_name=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_UserRegistration,on_delete=models.CASCADE)
class tbl_reference(models.Model):
    reference_name=models.CharField(max_length=50)
    reference_email=models.CharField(max_length=50)
    reference_contact=models.CharField(max_length=50)
    reference_relation=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_UserRegistration,on_delete=models.CASCADE)
class tbl_certificate(models.Model):
    certificate_name=models.CharField(max_length=50)
    certificate_upload=models.FileField(upload_to="Assets/User/")
    user=models.ForeignKey(tbl_UserRegistration,on_delete=models.CASCADE)
class tbl_Myprofile(models.Model):
    Myprofile_photo=models.FileField(upload_to="Assets/User/")
    Myprofile_name=models.CharField(max_length=50)
    Myprofile_email=models.CharField(max_length=50)
    Myprofile_contact=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_UserRegistration,on_delete=models.CASCADE)
class tbl_Changepassword(models.Model):
    Changepassword_oldpassword=models.CharField(max_length=50)
    Changepassword_newpasword=models.CharField(max_length=50)
    Changepassword_confirmpassword=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_UserRegistration,on_delete=models.CASCADE)
class tbl_Editprofile(models.Model):
    Editprofile_name=models.CharField(max_length=50)
    Editprofile_email=models.CharField(max_length=50)
    Editprofile_contact=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_UserRegistration,on_delete=models.CASCADE)
class tbl_cv(models.Model):
    cv_name=models.CharField(max_length=50)
    cv_email=models.CharField(max_length=50)
    cv_about=models.CharField(max_length=50)
    cv_contact=models.CharField(max_length=50)
    cv_address=models.CharField(max_length=50)
    cv_education=models.CharField(max_length=50)
    cv_experience=models.CharField(max_length=50)
    cv_skill=models.CharField(max_length=50)
    cv_hobbies=models.CharField(max_length=50)
    cv_reference=models.CharField(max_length=50)
    cv_language=models.CharField(max_length=50)
    cv_project=models.CharField(max_length=50)
    cv_certificate=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_UserRegistration,on_delete=models.CASCADE)

class tbl_Feedback(models.Model):
    Feedback_name=models.CharField(max_length=50)
    Feedback_email=models.CharField(max_length=50)
    Feedback_message=models.CharField(max_length=50) 
    user=models.ForeignKey(tbl_UserRegistration,on_delete=models.CASCADE)
