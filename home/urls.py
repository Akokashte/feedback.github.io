"""feedback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('login',views.handleLogin,name="handleLogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('signup',views.handleSignup,name="handleSignup"),
    path('about',views.about,name="about"),
    path('feedback',views.feedback,name="feedback"),
    path('report',views.report,name="report"),
    path('form',views.form,name="form"),
    path('practical',views.practical,name="practical"),
    # path('forgotpass',views.forgotpass,name="forgotpass"),

    path('parentsfeedback', views.parentsfeedback, name="parentsfeedback"),
    path('alumnifeedback', views.alumnifeedback, name="alumnifeedback"),
    
    path('form_select', views.form_select, name="form_select"),

    path('save_responses', views.save_responses, name="save_responses"),

]
