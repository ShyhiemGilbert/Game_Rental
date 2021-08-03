from django.http import HttpResponse
from django.shortcuts import render
from .models import Game


# Create your views here.

def index(request):
    games = Game.objects.all()  # SELECT * FROM games_game
    render(request, 'games/index.html', {'games': games})
