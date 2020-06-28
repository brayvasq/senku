from src.models.node import Node
from src.models.generator import Generator
from src.utils.bfs import BFS
from src.utils.dfs import DFS
from src.utils.greedy import Greedy
from src.utils.a_star import AStar

class Game:
    def __init__(self):
        self.root = self.__base_node()

    def process(self, option = "bfs"):
        if option == "user":
            self.user_game()
        elif option == "bfs":
            print("BFS Algorithm: Breadth First Search")
            BFS(self.root).run()
        elif option == "dfs":
            print("DFS Algorithm: Depth First Search")
            DFS(self.root).run()
        elif option == "greedy":
            print("Greedy Algorithm")
            Greedy(self.root).run()
        elif option == "astar":
            print("A*: A Star")
            AStar(self.root).run()

    # TODO: user game interaction
    def user_game(self):
        print("Error: Not implemented")

    def __base_node(self):
        senku = [
            ["_","_","_","_","1","_","_","_","_"],
            ["_","_","_","1","_","1","_","_","_"],
            ["_","_","1","_","1","_","1","_","_"],
            ["_","1","_","1","_","1","_","1","_"],
            ["0","_","1","_","1","_","1","_","1"]
        ]

        return Node(senku)

