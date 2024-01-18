from django.urls import path
from .views import *

app_name = 'cardgame'

urlpatterns = [
    path('', show_main, name="main_page"),
    path('play/', start_game, name="main_page"),
]