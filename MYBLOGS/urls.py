"""MYBLOGS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from BLOGS import views

from ACCOUNTS import views as accounts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name ='index'),
    path('<int:pk>', views.detail, name ='detail'),
    path('about/', views.about, name ='about'),
    path('contact', views.contact, name ='contact'),
    path('signup/', accounts_views.signup, name ='signup'),
    path('login/', accounts_views.login, name ='login'),
    path('comment/<int:pk>/', views.new_comment, name ='new_comment'),
]
