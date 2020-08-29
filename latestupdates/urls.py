from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.updateshome,name="updateshome"),
    path('<str:slug>', views.updatespost,name="updatespost"),
]