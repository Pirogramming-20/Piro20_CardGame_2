from django.urls import path
from .views import *

app_name = 'cardgame'

urlpatterns = [
    path('', show_main, name="main_page"),
    path('detail/<int:pk>', show_detail, name="game_detail"),
    path('play/', start_game, name='play_game'),
    path('list/', show_list, name="game_list"),
    path('cancel/<int:pk>', cancel_game, name="cancel_game"),
    path('accept/<int:pk>', accept_game, name="accept_game"),
    path('ranking/', show_ranking, name="ranking_page"),
]