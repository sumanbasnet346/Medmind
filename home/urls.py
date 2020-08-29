from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('contact',views.contact,name="conatct"),
    path('community',views.community,name="community"),
    path('search',views.search,name="search"),
    path('signup',views.handlesignup,name="handlesignup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handlelogout,name="handlelogout"),
]
