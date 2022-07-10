from django.contrib import admin
from django.urls import path,include
from .views import BaseInformation,UserRegister,cut_method,show_links
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',BaseInformation.as_view(), name='base-home'),
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name="Link/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="Link/logout.html"), name='logout'),
    path('show/', show_links,name='show'),
    path('test/', cut_method, name='test')

]