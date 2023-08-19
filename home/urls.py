from unicodedata import name
from django.urls import path
from . import views




urlpatterns = [
    path('', views.user_login, name='login_user'),
    path('home/',views.home,name='home'),
    path('logout/', views.user_logout, name= "logout"),
    path('userreg/',views.user_reg, name='userreg'),
    
]
