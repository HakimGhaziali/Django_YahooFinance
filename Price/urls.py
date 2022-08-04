from django.urls import path , include
from .views import fcreate

urlpatterns = [
    
    path('',fcreate , name ='priceshow'),
]
