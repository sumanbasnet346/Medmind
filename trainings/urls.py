from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name="home"),
    path('<str:title>', views.trainings,name="trainings"),
]