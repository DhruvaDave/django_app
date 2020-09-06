"""django_app URL Configuration

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
from django.urls import path, include
from student.views import AboutusTemplate,  StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentListView.as_view(),name="index"),
    # path('accounts/login/', auth_views.LoginView.as_view()),
     path('accounts/', include('django.contrib.auth.urls')),
    path('aboutus/', AboutusTemplate.as_view(),name="aboutus"),
    path('student/', StudentListView.as_view(),name="student_list"),
    path('student/<int:pk>', StudentDetailView.as_view(),name="student_detail"),
    path('student/create', StudentCreateView.as_view(),name="student_create"),
    path('student/<int:pk>/update', StudentUpdateView.as_view(),name="student_update"),
    path('student/<int:pk>/delete', StudentDeleteView.as_view(),name="student_delete"),
]
