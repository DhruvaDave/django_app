from django.conf.urls import url
from .views import AboutusTemplate
from django.urls import path


urlpatterns = [
    path('aboutus/', AboutusTemplate.as_view(),name="aboutus"),
]
