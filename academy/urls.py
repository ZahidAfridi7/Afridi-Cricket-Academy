from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("players/", views.all_player, name="all_player"),
    path("player/<int:id>/", views.player_details, name="player-details"),  
]
