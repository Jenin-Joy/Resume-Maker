from django.db import models
class tbl_Administrator(models.Model):
    Administrator_name=models.CharField(max_length=50);
    Administrator_email=models.CharField(max_length=50);
    Administrator_password=models.CharField(max_length=50);
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)
class tbl_language(models.Model):
    language=models.CharField(max_length=50)

