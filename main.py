from models.generator import Generator

if __name__ == "__main__":
    senku_matrix = [
        [-1,-1,-1,-1, 1,-1,-1,-1,-1],
        [-1,-1,-1, 1,-1, 1,-1,-1,-1],
        [-1,-1, 1,-1, 1,-1, 1,-1,-1],
        [-1, 1,-1, 1,-1, 1,-1, 1,-1],
        [ 0,-1, 1,-1, 1,-1, 1,-1, 1],
    ]

    g = Generator("Generador",senku_matrix)
    g.BFS(senku_matrix)