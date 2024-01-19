from django.urls import path
from .views import *

app_name = 'cardgame'

urlpatterns = [
    path('', show_base),
    path('history/', history),
]