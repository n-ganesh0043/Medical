from django.db import models

class Userregistrationmodel(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=40)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class adminmodel(models.Model):
    ad_username=models.CharField(max_length=20)
    ad_password=models.CharField(max_length=20)

class diseasemodel(models.Model):
    dis_name=models.CharField(max_length=20)
    sysmtoms=models.CharField(max_length=40)

class medicalmodels(models.Model):
    des_name=models.CharField(max_length=20)
    sysm=models.CharField(max_length=50)
    med_name=models.CharField(max_length=20)
    med_desp=models.CharField(max_length=100)
