from models.generator import Generator
from models.node import Node
from algoritms.algorithm import Algorithm

class BFS(Algorithm):

    def __init__(self,senku_matrix):
        Algorithm.__init__(self,senku_matrix)
    
    def run(self):
        print("Generando !!")
        buscar = True
        pasos = 0

        temp = self.senku_matrix[:]
        state = Node(temp)
        
        frontera = [state]
        visitados = {}
        
        while(buscar and len(frontera)>0):
            pasos += 1
            #print(pasos)
            nodo = frontera[0]
            nodo.step = pasos
            nodo.name = "Nodo : "+str(nodo.step)
            frontera.pop(0)
            #nodo.print_matrix()
            if not list(visitados.values()).__contains__(nodo):
                visitados[nodo.step] = nodo
            vecinos = self.obtener_vecinos(nodo,list(visitados.values()),frontera)
            #print(vecinos)
            for i in vecinos:
                i.parent_id = nodo.step

            if(self.verify_win(nodo.matrix)):
                #print("Termino")
                buscar = False
            else:
                pass
                #print("Buscando")
                #hijos[nodo.name] = vecinos

            for i in vecinos:
                frontera.append(i) 

        #return [nodo,visitados]
        return self.path([nodo,visitados])
    
    def path(self,lista):
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
        
        return camino
