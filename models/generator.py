from models.node import Node

class Generator:
    """
        :version: 0.1
        This class have the logic of the game puzzle
    """

    def __init__(self,name,root):
        self.name = name
        self.root = root

    def verify_pos(self,end,middle,start,matrix):
        """
           This method verify that the positions don't exceed 
           the limits of the matrix

           :param: end, destination position
           :param: middle, position of item to eliminate
           :param: start, position of item to move

           :return: True if the positions are between the limits, False if not
        """
        pos_x_down = end[1] >= 0 and middle[1] >= 0 and start[1]>=0
        limit_x    = len(matrix[0])
        pos_x_top  = end[1] < limit_x  and middle[1] < limit_x and start[1] < limit_x

        pos_y_down = end[0] >= 0 and middle[0] >= 0 and start[0] >= 0
        limit_y    = len(matrix)
        pos_y_top  = end[0] < limit_y and middle[0] < limit_y and start[0] < limit_y

        return pos_x_down and pos_x_top and pos_y_down and pos_y_top

    def verify_values(self,end,middle,start,matrix):
        """
            This method verify if exist a valid move from three positions

            :param: end, destination position
            :param: middle, position of item to eliminate
            :param: start, position of item to move

            :return: True if exist a valid move, False if not
        """
        return matrix[end[0]][end[1]] == 0 and matrix[middle[0]][middle[1]] == 1 and matrix[start[0]][start[1]] == 1

    def generate_matrix_state(self,start,middle,end,matrix):
        resp = None

        if(self.verify_pos(start,middle,end,matrix) and self.verify_values(start,middle,end,matrix)):
            matrix[start[0]][start[1]]   = 1
            matrix[middle[0]][middle[1]] = 0
            matrix[end[0]][end[1]]       = 0
            resp = matrix
        
        return resp

    def move_right(self,pos,matrix):
        temp_matrix = matrix[:]
        temp = self.generate_matrix_state([pos[0],pos[1]],[pos[0],pos[1]+2],[pos[0],pos[1]+4],temp_matrix)
        return temp

    def move_left(self,pos,matrix):
        temp_matrix = matrix[:]
        temp = self.generate_matrix_state([pos[0],pos[1]],[pos[0],pos[1]-2],[pos[0],pos[1]-4],temp_matrix)
        return temp

    def diagonal_up_right(self,pos,matrix):
        temp_matrix = matrix[:]
        temp = self.generate_matrix_state([pos[0],pos[1]],[pos[0]-1,pos[1]+1],[pos[0]-2,pos[1]+2],temp_matrix)
        return temp
    
    def diagonal_up_left(self,pos,matrix):
        temp_matrix = matrix[:]
        temp = self.generate_matrix_state([pos[0],pos[1]],[pos[0]-1,pos[1]-1],[pos[0]-2,pos[1]-2],temp_matrix)
        return temp

    def diagonal_down_right(self,pos,matrix):
        temp_matrix = matrix[:]
        temp = self.generate_matrix_state([pos[0],pos[1]],[pos[0]+1,pos[1]+1],[pos[0]+2,pos[1]+2],temp_matrix)
        return temp
    
    def diagonal_down_left(self,pos,matrix):
        temp_matrix = matrix[:]
        temp = self.generate_matrix_state([pos[0],pos[1]],[pos[0]+1,pos[1]-1],[pos[0]+2,pos[1]-2],temp_matrix)
        return temp

    def copiar(self,matrix):
        copia = []
        for fila in matrix:
            aux = fila.copy()
            copia.append(aux)
        return copia
    
    def add_state(self,resp,list_states):
        if(resp!=None):
            list_states.append(resp)

    def get_state_for_pos(self,pos,matrix):
        list_states = []
        temp = self.copiar(matrix)
        resp = self.move_right(pos,temp)
        self.add_state(resp,list_states)
        temp = self.copiar(matrix)
        resp = self.move_left(pos,temp)
        self.add_state(resp,list_states)
        temp = self.copiar(matrix)
        resp = self.diagonal_up_right(pos,temp)
        self.add_state(resp,list_states)
        temp = self.copiar(matrix)
        resp = self.diagonal_up_left(pos,temp)
        self.add_state(resp,list_states)
        temp = self.copiar(matrix)
        resp = self.diagonal_down_right(pos,temp)
        self.add_state(resp,list_states)
        temp = self.copiar(matrix)
        resp = self.diagonal_down_left(pos,temp)
        self.add_state(resp,list_states)
        return list_states

    def get_pos_play(self,matrix):
        list_pos = []
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if(matrix[i][j] == 0):
                    list_pos.append([i,j])
        return list_pos
    
    

    def BFS(self,matrix):
        print("Generando !!")
        buscar = True
        pasos = 0

        temp = matrix[:]
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

        return [nodo,visitados]
        
    