"""medicalproject URL Configuration

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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='main'),
    path('user_registration/',views.user_registration.as_view(),name='user_registration'),
    path('adminpage/',views.adminpage.as_view(),name='admin'),
    path('disease_home_page/',views.disease_home_page.as_view(),name='disease_home_page'),
    path('delete_des/',views.delete_des,name='delete_des'),
    path('update_des/',views.update_des,name='update_des'),
    path('updated_des/',views.updated_des,name='updated_des'),
    path('medicene_page/',views.medicene_page.as_view(),name='medicene_page'),
    path('delete_med/',views.delete_med,name='delete_med'),
    path('update_med/',views.update_med,name='update_med'),
    path('updated_med/',views.updated_med,name='updated_med'),
    path('reports_adm/',views.reports_adm,name='reports_adm'),
    path('user_login/',views.user_login.as_view(),name='user_login'),
    path('report_usr/',views.report_usr,name='report_usr'),
    path('srch_med/',views.srch_med.as_view(),name='srch_med'),
    path('change_pswd/',views.change_pswd.as_view(),name='change_pswd')
]
