from django.urls import path
from rest_framework.decorators import api_view
from todo.API import views as api_views

urlpatterns = [

    path('kullanicilar/',api_views.kullanicilar_list_create_api_view, name='kullanicilar' ),
    path('kullanicilar/<int:pk>',api_views.kullanicilar_detail_api_view,name='kul-detay'),
    path('turler/',api_views.turler_list_create_api_view,name="Turler"),
    path('turler/<int:pk>',api_views.turler_detail_api_view,name="Turdetay"),
     path('courses/',api_views.courses,name='courses'),
    path('courses/<int:pk>',api_views.courses_detail,name='coursesdetail'),
    
]
