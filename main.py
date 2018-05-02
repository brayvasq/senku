from algoritms.bfs import BFS
from algoritms.dfs import DFS

if __name__ == "__main__":
    senku_matrix = [
        [-1,-1,-1,-1, 1,-1,-1,-1,-1],
        [-1,-1,-1, 1,-1, 1,-1,-1,-1],
        [-1,-1, 1,-1, 1,-1, 1,-1,-1],
        [-1, 1,-1, 1,-1, 1,-1, 1,-1],
        [ 0,-1, 1,-1, 1,-1, 1,-1, 1],
    ]

    g = BFS(senku_matrix)
    g.run()
    print("-----------------------------------------")
    g = DFS(senku_matrix)
    g.run()

     