from django.urls import include, path
from rest_framework import routers
from .import views

router=routers.DefaultRouter()

urlpatterns = [
    path('', views.home, name='chat'),
    path('api/get_response/', views.get_response, name='chat')
    #path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
