"""
URL configuration for lesson1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path
from demo.views import index, time, hello, sum, index2, pagi  # , timetwo

#from demo.views import users

urlpatterns = {
    path('admin/', admin.site.urls),
    path('', index),
    path('time/', time),
    path('hello/', hello),
    path('sum/<int:op1>/<int:op2>/', sum),
    path('index/', index2),
    path('pagi/', pagi)

}
