from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_esep',add_esep,name='add_esep')
]
