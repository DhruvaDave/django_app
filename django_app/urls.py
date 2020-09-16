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
# from student.api_views import StudentAPIList
from student.api_views import api_root, StudentHighlight, StudentList, StudentDetail, StudentAPIList, UserList, UserDetail, StudentViewSet, UserViewSet
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import renderers

student2_list = StudentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
student2_detail = StudentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
student2_highlight = StudentViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user2_list = UserViewSet.as_view({
    'get': 'list'
})
user2_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentListView.as_view(), name="index"),
    # path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('aboutus/', AboutusTemplate.as_view(), name="aboutus"),
    path('student/', StudentListView.as_view(), name="student_list"),
    path('student/<int:pk>', StudentDetailView.as_view(), name="student_detail"),
    path('student/create', StudentCreateView.as_view(), name="student_create"),
    path('student/<int:pk>/update',
         StudentUpdateView.as_view(), name="student_update"),
    path('student/<int:pk>/delete',
         StudentDeleteView.as_view(), name="student_delete"),

    # Class View
    # path('studentapi/', StudentAPIList.as_view(),name="studentapi-list"),
    # path('studentapi/<int:pk>/', StudentDetail.as_view(),name="studentapi-detail"),

    # Generic Class view
    path('studentapi/', StudentList.as_view(), name="studentapi-list"),
    path('studentapi/<int:pk>/', StudentDetail.as_view(), name="studentapi-detail"),

    path('users/', UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', UserDetail.as_view()),

    path('studentapi/<int:pk>/highlight/', StudentHighlight.as_view()),
    path('all/', api_root),

    path('student2/', student2_list, name='student2-list'),
    path('student2/<int:pk>/', student2_detail, name='student2-detail'),
    path('student2/<int:pk>/highlight/', student2_highlight, name='student2-highlight'),
    path('users2/', user2_list, name='user2-list'),
    path('users2/<int:pk>/', user2_detail, name='user2-detail')

    # path('studentapi/<int:pk>/', views.SnippetDetail.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
