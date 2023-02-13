
from django.urls import path
from .import views 

urlpatterns = [
    path('',views.javed,name='javed'),
    path('result',views.details,name='javed'),
  
    
]


# Total: 12