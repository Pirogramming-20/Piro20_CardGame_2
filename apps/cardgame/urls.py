from django.urls import path
from .views import *

urlpatterns = [
    path('', show_base),
    path('history/', history),
]