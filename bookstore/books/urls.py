from django.urls import path
from . import views
app_name= "books"

urlpatterns=[

    path('home', views.home, name="home1"),
    path('blist/', views.booklist, name="blist"),
    path('profile/', views.profile, name="profile"),
    path('master/', views.master, name="master"),
    path('login/', views.login, name="cust_login"),
    path('cust_reg/', views.custreg, name="cust_reg"),
   

    
]