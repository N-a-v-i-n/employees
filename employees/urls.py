"""employees URL Configuration

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
from temp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('view_all/',views.view_all,name='view_all'),
    path('update_emp/',views.update_emp,name="update_emp"),
    path('filter_emp',views.filter_emp,name="filter_emp"),
    path('delete_emp',views.delete_emp,name="delete_emp"),
    path('add_emp',views.add_emp,name="add_emp"),
    path('update_emp/<int:employee_id>',views.update_emp),
    path('otp_verify/',views.otp_verify)
    
]
