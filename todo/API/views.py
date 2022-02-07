from rest_framework import serializers, status,permissions
from rest_framework.exceptions import PermissionDenied

from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from todo.models import Courses, Kullanci, k_Turu
from todo.API.serializer import  CoursesSerializer, KullaniciSerializer, TurlerSerializer,RegistrationSerializer
from rest_framework.authtoken.models import Token

#Kullanıcılara ulaşabilmek için



@api_view(['GET','POST','UPDATE'])
def kullanicilar_list_create_api_view(request):
#POST VE GETİ BİRBİRİNDEN AYIRACAKSIN  ÖNEMLİ  --------------------------------------------------------------------------------
    if request.method == 'GET':
        kullanicilar= Kullanci.objects.all() 
        serializer= KullaniciSerializer(kullanicilar,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  
        
        serializer = KullaniciSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
 
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  # Kullanicilar içindeki verilere ulaşmak için
#@api_view(['POST'])
#def api_create_user_view(request):
  #      if request.method =='POST':
   #         serializer = KullaniciSerializer(data=request.data)
    #        if serializer.is_valid():
     #           serializer.save()
      #          return Response(serializer.data,status = status.HTTP_201_CREATED)
       #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','UPDATE'])
def courses(request):

    if request.method == 'GET':
        courses= Courses.objects.all() 
        serializer= CoursesSerializer(courses,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  # Kullanicilar içindeki verilere ulaşmak için

@api_view(['GET','PUT','DELETE'])
def courses_detail(request,pk):
    try:
        courses_instance = Courses.objects.get(pk=pk)
    except Kullanci.DoesNotExist:
        return Response({
            'errors': {
                'code': 404,
                'message': f'Kullanıcı bulunamadı',
                
           }
        },
        status=status.HTTP_400_BAD_REQUEST
        )
    
    if request.method== 'GET':
        serializer= CoursesSerializer(courses_instance)
        return Response(serializer.data)

    elif request.method=='PUT':
         serializer = CoursesSerializer(courses_instance, data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
         courses_instance.delete()
         return Response(
             {
                'işlem':{
                    'code': 204,
                    'message': f'({pk}) id numaralı kurs silinmiştir'
                },

             },
             status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def kullanicilar_detail_api_view(request, pk):
    try:
        kullanici_instance = Kullanci.objects.get(pk=pk)
    except Kullanci.DoesNotExist:
        return Response({
            'errors': {
                'code': 404,
                'message': f'Kullanıcı bulunamadı',
                
           }
        },
        status=status.HTTP_400_BAD_REQUEST
        )
    
    if request.method== 'GET':
        serializer= KullaniciSerializer(kullanici_instance)
        return Response(serializer.data)

    elif request.method=='PUT':
         serializer = KullaniciSerializer(kullanici_instance, data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
         kullanici_instance.delete()
         return Response(
             {
                'işlem':{
                    'code': 204,
                    'message': f'({pk}) id numaralı kullanıcı silinmiştir'
                },

             },
             status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST','UPDATE'])
def turler_list_create_api_view(request):

    if request.method == 'GET':
        turlerr= k_Turu.objects.all() 
        serializer= TurlerSerializer(turlerr,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TurlerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def turler_detail_api_view(request, pk):
    try:
        turler_instance = k_Turu.objects.get(pk=pk)
    except k_Turu.DoesNotExist:
        return Response({
            'errors': {
                'code': 404,
                'message': f'Kullanıcı bulunamadı',
                
           }
        },
        status=status.HTTP_400_BAD_REQUEST
        )
    
    if request.method== 'GET':
        serializer= TurlerSerializer(turler_instance)
        return Response(serializer.data)

    elif request.method=='PUT':
         serializer = TurlerSerializer(turler_instance, data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
         turler_instance.delete()
         return Response(
             {
                'işlem':{
                    'code': 204,
                    'message': f'({pk}) id numaralı kullanıcı silinmiştir'
                },

             },
             status=status.HTTP_204_NO_CONTENT)