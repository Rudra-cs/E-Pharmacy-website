from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('admin',views.adminpage,name="adminpage"),
    
]