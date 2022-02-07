
from django.contrib import admin
from todo.API.views import courses

from todo.models import  Courses, Ilgi_Alanlari, k_Turu, Kullanci,  Ogrenci, Ogretmen, Randevular

# Register your models here.
admin.site.register(Kullanci)
admin.site.register(k_Turu)
admin.site.register(Ogrenci)
admin.site.register(Ogretmen)
admin.site.register(Randevular)
admin.site.register(Ilgi_Alanlari)
admin.site.register(Courses)
