from distutils.command.upload import upload


from enum import auto

from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case, Value
from django.db.models.fields import files
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from rest_framework.authtoken.models import Token
from django.dispatch import receiver 
from django.db.models.signals import post_save


class k_Turu(models.Model):
    K_Turu = models.CharField(verbose_name="Tur", null=False, max_length=35, default="nonEmail")
  
    def __str__(self):
        return self.K_Turu
    
def generate_filename(self,filename):
    url="files/users/%s/%s"%(self.id,filename)
    return url


class Ilgi_Alanlari(models.Model):
    alan_Adi = models.CharField(max_length=35)
    def __str__(self):
        return self.alan_Adi

# Create your models here.
class Kullanci(models.Model):
    k_email = models.EmailField(verbose_name="E-mail", null=False, default="nonEmail")
    k_adi = models.CharField(verbose_name="k_adi", max_length=35, null=False, default="nonEmail")
    k_soyadi = models.CharField(verbose_name="soyadi", max_length=35, null=False, default="nonEmail")
    k_sifre = models.CharField(null=False, max_length=35, default="nonEmail")
    k_Turu= models.ForeignKey(k_Turu, on_delete= models.CASCADE,related_name='KullaniciTurleri',default='1')
    k_avatar=models.ImageField(upload_to=generate_filename,blank=True,default=None)
    k_ilgi = models.ManyToManyField(Ilgi_Alanlari,related_name='Ilgi_Alanlari',default=None)
    def __str__(self):
       return str(self.id)
   

def generate_for_filname_teacher(self,filename):
    url="files/users/%s/%s"%(self.k_id,filename)
    return url


class Ogretmen(models.Model):
    k_id = models.OneToOneField(Kullanci, on_delete=CASCADE)
    ogr_tanitim = models.FileField(upload_to=generate_for_filname_teacher)
    stars = models.FloatField()
       
def generate_filename_coursePhoto(self,filename):
        url="files/users/%s/%s"%(self.courseName,filename)
        return url
class Courses(models.Model):
    courseName= models.CharField(verbose_name="CourseName",null=False,max_length=50,default="Please enter course name")
    coursePhoto = models.ImageField(upload_to=generate_filename_coursePhoto,blank=True,default=None)
    coursePrice= models.IntegerField()
    courseAuthor= models.ForeignKey(Ogretmen,on_delete=models.CASCADE,related_name="Teacher",default="1" )
    def __str__(self):
        return self.courseName


   
class Ogrenci(models.Model):
    k_id = models.ForeignKey(Kullanci, on_delete=CASCADE)
    stars = models.FloatField()
    


class Randevular(models.Model):
    ogretmen_randevu = models.ForeignKey(Ogretmen, on_delete=CASCADE)
    ogrenci_randevu = models.ForeignKey(Ogrenci, on_delete=CASCADE)
    ders_tarihi = models.DateField()


    


