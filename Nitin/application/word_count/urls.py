from django.urls import path
from . import views


urlpatterns = [
    path('about', views.application, name='appli' )
]