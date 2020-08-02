from django.shortcuts import render
from .models import Game
from .serializers import GameSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .node import Node
from .bfs import BFS
from .dfs import DFS
from .greedy import Greedy
from .a_star import AStar
# solver = Senku()

# Create your views here.
class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def post(self, request, *args, **kwargs):
        algorithm = request.data["algorithm"]
        # global solver
        print(request.data)

        senku = request.data["initial"]

        result = []
        if algorithm == 'bfs':
            result = BFS(Node(senku)).run()
        elif algorithm == 'dfs':
            result = DFS(Node(senku)).run()
        elif algorithm == 'greedy':
            result = Greedy(Node(senku)).run()
        elif algorithm == 'a_star':
            result = AStar(Node(senku)).run()

        result = list(map(lambda x: x.matrix, result))

        return Response(data=result, status=status.HTTP_201_CREATED)
