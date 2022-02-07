from urllib import response
from venv import create
from django.contrib.auth import login
from django.shortcuts import render
from matplotlib.style import context
from numpy import generic
from knox.models import AuthToken
from rest_framework.authtoken.models import Token
from accounts.serializers import *
from rest_framework.response import Response
from knox.views import LoginView as KnoxLoginView
from .serializers import UserSerializer,RegistrationSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import generics,permissions
# Create your views here.

class RegisterAPI(generics.GenericAPIView):
    serializer_class=RegistrationSerializer

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
          }  )


class LoginAPI(KnoxLoginView):
    permissions_classes=(permissions.AllowAny,)

    def post(self,request,format=None):
        serializer=AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)