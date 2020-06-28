from src.models.node import Node
from src.models.generator import Generator
from src.utils.bfs import BFS
from src.utils.dfs import DFS
from src.utils.greedy import Greedy
from src.utils.a_star import AStar

class Game:
    def __init__(self, option = 1):
        self.option = option
        self.root = self.__base_node()

    def process(self, option):
        if self.option == 1:
            self.user_game()
        elif self.option == 2:
            print("BFS Algorithm: Breadth First Search")
            BFS(self.root).run()
        elif self.option == 3:
            print("DFS Algorithm: Depth First Search")
            DFS(self.root).run()
        elif self.option == 4:
            print("Greedy Algorithm")
            Greedy(self.root).run()
        elif self.option == 5:
            print("A*: A Star")
            AStar(self.root).run()

    # TODO: user game interaction
    def user_game(self):
        pass

    def __base_node(self):
        senku = [
            ["_","_","_","_","1","_","_","_","_"],
            ["_","_","_","1","_","1","_","_","_"],
            ["_","_","1","_","1","_","1","_","_"],
            ["_","1","_","1","_","1","_","1","_"],
            ["0","_","1","_","1","_","1","_","1"]
        ]

        return Node(senku)

