from models.generator import Generator
from models.node import Node

class Algorithm:

    def __init__(self,senku_matrix):
        self.name = ""
        self.senku_matrix = senku_matrix
        self.generator = Generator("Generador",self.senku_matrix)

    def verify_win(self,matrix):
        num_pos=0
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if(matrix[i][j] == 1):
                    num_pos += 1

        return num_pos == 1

    def find_win(self,vecinos):
        resp = False
        if(vecinos != None):
            for i in vecinos:
                resp = self.verify_win(i.matrix)
                if(resp):
                    break
        return resp
    
    def obtener_vecinos(self,nodo,visitados,frontera):
        list_pos = self.generator.get_pos_play(nodo.matrix)
        #print(list_pos)
        list_states = []
        for i in list_pos:
            states = self.generator.get_state_for_pos(i,nodo.matrix)
            for state in states:
                #print(state)
                node_state = Node(state) 
                if (not list_states.__contains__(node_state)) and (not visitados.__contains__(node_state)) and (not frontera.__contains__(node_state)) : 
                    list_states.append(node_state)
        return list_states

    def run():
        pass

    def path():
        pass