from django.shortcuts import render
from .models import Game
from .serializers import GameSerializer
from rest_framework import generics

# Create your views here.
class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
