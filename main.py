from algoritms.bfs import BFS
from algoritms.dfs import DFS
from algoritms.greedy import Greedy
from algoritms.a_star import AStar

if __name__ == "__main__":
    senku_matrix = [
        [-1,-1,-1,-1, 1,-1,-1,-1,-1],
        [-1,-1,-1, 1,-1, 1,-1,-1,-1],
        [-1,-1, 1,-1, 1,-1, 1,-1,-1],
        [-1, 1,-1, 1,-1, 1,-1, 1,-1],
        [ 0,-1, 1,-1, 1,-1, 1,-1, 1],
    ]

    #g = BFS(senku_matrix)
    #g.run()
    print("-----------------------------------------")
    #g = DFS(senku_matrix)
    #g.run()
    print("-----------------------------------------")
    #g = Greedy(senku_matrix)
    #g.run()
    print("-----------------------------------------")
    g = AStar(senku_matrix)
    g.run()
     