
from django.shortcuts import render,get_object_or_404
from .models import Players


def starting_page(request):
    all_players = Players.objects.all()
    return render(request, 'academy/include/home.html', {
        'players': all_players
    })

def all_player(request):
    players = Players.objects.all()
    return render(request, 'academy/include/all-player.html', {
        'all_player': players
    })

def player_details(request, id):
    selected_player = get_object_or_404(Players,id)
    return render(request , 'academy/include/player_details.html')
    