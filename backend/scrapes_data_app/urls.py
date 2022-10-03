



from django.contrib import admin
from django.urls import include, path

from scrapes_data_app import views
from rest_framework import viewsets, routers



router = routers.DefaultRouter()

#router.register(r'index',views.WebscrapViewSet,basename="index")
router.register(r'list',views.WebscrapViewSet,basename="list")
router.register(r'post',views.WebscrapViewSet,basename="post")



app_name='scrapes_data_app'

urlpatterns = [
    path('', include(router.urls)),
    
]
        
   
   