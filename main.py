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
    lista = g.BFS(senku_matrix)

    valor = lista[0]
    visitados = lista[1]

    parent = valor.step
    camino = []
    print(type(visitados))
    #visitados[3000].print_matrix()
    while(parent > 1):
        nodo = visitados[parent]
        camino.append(nodo)
        parent = nodo.parent_id
    
    camino = camino[::-1]
    print(len(camino))
    for i in camino:
        i.print_matrix()
        