"""TeleNumInquiry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from TestModleApp import views
urlpatterns = [
    path('', views.mylogin, name="mylogin"),
    path('admin/', admin.site.urls),
    path('mylogin/', views.mylogin, name="mylogin"),
    path('mylogout', views.mylogout,name ="mylogout"),
    path('kjfs_search/', views.kjfs_search, name="kjfs_search"),
    path('ceshi/', views.ceshi, name="ceshi"),
    path('showtable/', views.showtable, name="showtable"),
    path('kjfs_edit/', views.kjfs_edit, name="kjfs_edit"),
    path('fileupload/', views.fileupload, name="fileupload"),
    path('download/', views.download, name="download"),
    path('cdh/', views.cdh, name="cdh"),
]
