
from dataclasses import field
from datetime import datetime
import email
from os import name
from select import select
from typing_extensions import Required
from django.db import models
from django.db.models import fields
from matplotlib import style
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from accounts.serializers import RegistrationSerializer
from todo.models import Courses, Ilgi_Alanlari, Kullanci, Ogrenci, Ogretmen, Randevular, k_Turu


      
# API için serilizasyon modeli
class OgretmenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Ogretmen
        fields="__all__"
        read_only_fiels=["id"] 
    def create(self,validated_data):
     return Ogretmen.objects.create(**validated_data)




class OgrenciSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ogrenci
        fields="__all__"
        read_only_fiels=["id"]
    def create(self,validated_data):
        return Ogrenci.objects.create(**validated_data)


class RandevularSerializer(serializers.ModelSerializer):
    class Meta:
        model= Randevular
        fields="__all__"
        read_only_fiels=["id"]
    def create(self,validated_data):
        return Randevular.objects.create(**validated_data)
    def validate(self,data):
        if data['ders_tarihi']<datetime.now():
            raise serializers.ValidationError(
            'Randevu tarihiniz günümüz tarihinden önce olamaz.'
        )
    
        return data


class IlgiAlanlariSerializer(serializers.ModelSerializer):
    class Meta:
        model= Ilgi_Alanlari
        fields="__all__"
        read_only_fields=["id"]
    def create(self, validated_data):
        return Ilgi_Alanlari.objects.create(**validated_data)


class TurlerSerializer(serializers.ModelSerializer):
    class Meta:
        model=k_Turu
        fields="__all__"
        read_only_fieds=["id"]



class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields="__all__"
        ReadOnlyField=['id']

class KullaniciSerializer(serializers.ModelSerializer):
  
    
    class Meta:
        model=Kullanci
        fields='__all__'
        read_only_fields=['id']
     

    def validate(self,data):
        if data['k_adi']==data['k_soyadi']:
         raise serializers.ValidationError(
            'Ad ve Soyad aynı olamaz Lütfen farklı ad veya soyad giriniz..',
        )  
       
        return data    

    

    def create(self, validated_data):
        
        RegistrationSerializer.save(**validated_data)
        return Kullanci.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.k_email=validated_data.get('k_email',instance.k_email)
        instance.k_adi=validated_data.get('k_adi',instance.k_adi)
        instance.k_soyadi=validated_data.get('k_soyadi', instance.k_soyadi)
        instance.k_sifre=validated_data.get('k_sifre',instance.k_sifre)
        instance.k_turu=validated_data.get('k_turu',instance.k_turu)
        instance.k_ilgi=validated_data.get('k_ilgi',instance.k_ilgi)
        instance.save()
        return instance
    
      
 #Custom Validate Ad Soyad Eşit olamaz

    def validate(self,data):
        if data['k_adi']==data['k_soyadi']:
         raise serializers.ValidationError(
            'Ad ve Soyad aynı olamaz Lütfen farklı ad veya soyad giriniz..',
        )
        return data
    