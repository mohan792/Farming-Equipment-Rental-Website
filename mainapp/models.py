import email
from tkinter.tix import Tree
from django.db import models

# Create your models here.
class infoofuser(models.Model):
    s_no=models.AutoField
    user_id=models.IntegerField(null=True)
    username=models.CharField(max_length=75,default="")
    password=models.CharField(max_length=75,default="")
    email=models.CharField(max_length=75,default="")
    latitude=models.FloatField(null=True)
    longitude=models.FloatField(null=True)
    village=models.CharField(max_length=75,default="")
    taluka=models.CharField(max_length=75,default="")
    district=models.CharField(max_length=75,default="")
    phone_no=models.IntegerField(null=True)
    def __str__(self):
        return self.username
class equipment(models.Model):
    s_no=models.AutoField
    equipmentholder_id=models.IntegerField(null=True)
    equipment_id=models.IntegerField(null=True)
    username=models.CharField(max_length=75,default="")
    password=models.CharField(max_length=75,default="")
    latitude=models.FloatField(null=True)
    longitude=models.FloatField(null=True)
    phone_no=models.IntegerField(null=True)
    village=models.CharField(max_length=75,default="")
    taluka=models.CharField(max_length=75,default="")
    district=models.CharField(max_length=75,default="")
    company=models.CharField(max_length=75,default="")
    old=models.IntegerField(null=True)
    equipmentname=models.CharField(max_length=75,default="")
    rent=models.IntegerField()
    image1= models.ImageField(upload_to="mainapp/images",default="")
    image2= models.ImageField(upload_to="mainapp/images",default="")
    image3= models.ImageField(upload_to="mainapp/images",default="")
    image4= models.ImageField(upload_to="mainapp/images",default="")
    def __str__(self):
        return self.username
class equipment1(models.Model):
    s_no=models.AutoField
    equipmentholder_id=models.IntegerField(null=True)
    equipment_id=models.IntegerField(null=True)
    username=models.CharField(max_length=75,default="")
    password=models.CharField(max_length=75,default="")
    latitude=models.FloatField(null=True)
    longitude=models.FloatField(null=True)
    phone_no=models.IntegerField(null=True)
    village=models.CharField(max_length=75,default="")
    taluka=models.CharField(max_length=75,default="")
    district=models.CharField(max_length=75,default="")
    company=models.CharField(max_length=75,default="")
    old=models.IntegerField(null=True)
    equipmentname=models.CharField(max_length=75,default="")
    rent=models.IntegerField()
    image1= models.ImageField(upload_to="mainapp/images",default="")
    image2= models.ImageField(upload_to="mainapp/images",default="")
    image3= models.ImageField(upload_to="mainapp/images",default="")
    image4= models.ImageField(upload_to="mainapp/images",default="")
    def __str__(self):
        return self.username
class requests(models.Model):
    applicant_name=models.CharField(max_length=75,default="")
    applicant_village=models.CharField(max_length=75,default="")
    applicant_taluka=models.CharField(max_length=75,default="")
    applicant_phone=models.CharField(max_length=75,default="")
    applicant_lat=models.FloatField(null=True)
    applicant_long=models.FloatField(null=True)
    equipment_name=models.CharField(max_length=75,default="")
    equipment_id=models.IntegerField(null=True)
    equipment_holder_phone_no=models.IntegerField(null=True)
    rent=models.IntegerField(null=True)
    take_date=models.CharField(max_length=75,default="")
    give_date=models.CharField(max_length=75,default="")
    total_rent=models.IntegerField(null=True)
class requests_apply(models.Model):
    applicant_name=models.CharField(max_length=75,default="")
    applicant_id=models.IntegerField(null=True)
    applicant_village=models.CharField(max_length=75,default="")
    applicant_taluka=models.CharField(max_length=75,default="")
    applicant_district=models.CharField(max_length=75,default="")
    applicant_phone=models.CharField(max_length=75,default="")
    equipment_name=models.CharField(max_length=75,default="")
    equipment_id=models.IntegerField(null=True)
    equipmentholder_phone_no=models.IntegerField(null=True)
    equipmentholder_id=models.IntegerField(null=True)
    equipmentholder_name=models.CharField(max_length=75,default="")
    equipmentholder_village=models.CharField(max_length=75,default="")
    equipmentholder_taluka=models.CharField(max_length=75,default="")
    equipmentholder_district=models.CharField(max_length=75,default="")
    rent=models.IntegerField(null=True)
    take_date=models.CharField(max_length=75,default="")
    give_date=models.CharField(max_length=75,default="")
    total_rent=models.IntegerField(null=True)
    request_status=models.CharField(max_length=75,default="Pending")
    def __str__(self):
        return self.applicant_name
