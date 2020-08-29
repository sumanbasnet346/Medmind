from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('contact',views.contact,name="conatct"),
    path('community',views.community,name="community"),
    path('search',views.search,name="search"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
]
