def verify_pos(start,middle,end,matrix):
    """ Verifica que las posiciones sean válidas dentro de la matriz en cuanto a tamaño de esta 
    @param start Posición a la cual moveríamos la bola en el movimiento
    @param middle Posición por la cual una bola "salta" a otra
    @param end Posicón de la bola que se quiere mover
    @param matrix Matriz que representa el estado actual
    return Retorna 1 o 0 si las posiciones son válidas para un nuevo movimiento """
    pos_x_down = start[1] >= 0 and middle[1] >= 0 and end[1] >= 0
    pos_x_top = start[1] < len(matrix[0]) and middle[1] < len(matrix[0]) and end[1] < len(matrix[0])

    pos_y_down = start[0] >= 0 and middle[0] >= 0 and end[0] >= 0
    pos_y_top = start[0] < len(matrix) and middle[0] < len(matrix) and end[0] < len(matrix)

    return pos_x_down and pos_x_top and pos_y_down and pos_y_top

def verify_vals(start,middle,end,matrix):
    """ Verifica que exista un movimiento válido a partir de tres posiciones 
    @param start Posición a la cual moveríamos la bola en el movimiento
    @param middle Posición por la cual una bola "salta" a otra
    @param end Posicón de la bola que se quiere mover
    @param matrix Matriz que representa el estado actual
    return Retorna 1 o 0 si las posiciones son válidas para un nuevo movimiento
    """
    return matrix[start[0]][start[1]] == 0 and matrix[middle[0]][middle[1]] == 1 and matrix[end[0]][end[1]] == 1

def print_matrix(matrix):
    """ Recorre e imprime una matriz por consola 
    @param matrix Matriz que representa el estado actual
    """
    if(matrix!=None):
        for i in matrix:
            print(i)
        print("\n")

def generate_matrix_state(start,middle,end,matrix):
    """ Se verifica que a partir de 3 posiciones exista un movimiento válido, si existe, se general el movimiento y se hace el moviiento
    @param start Posición a la cual moveríamos la bola en el movimiento
    @param middle Posición por la cual una bola "salta" a otra
    @param end Posicón de la bola que se quiere mover
    @param matrix Matriz que representa el estado actual
    return resp Retorna none si no existe un nuevo movimiento o la matriz si lo existe
    """
    resp = None
    if(verify_pos(start,middle,end,matrix) and verify_vals(start,middle,end,matrix)):
        matrix[start[0]][start[1]] = 1
        matrix[middle[0]][middle[1]] = 0
        matrix[end[0]][end[1]] = 0
        resp = matrix
    return resp

def move_right(pos,matrix):
    """ Verifica que exista un movimiento válido hacia la derecha
    @param pos Posición vacía dentro de la matriz
    @param matrix Matriz que representa el estado actual
    return Retorna none si existe un movimiento válido o la matriz si existe
    """
    temp_matrix = matrix[:]
    temp = generate_matrix_state([pos[0],pos[1]],[pos[0],pos[1]+2],[pos[0],pos[1]+4],temp_matrix)
    #print_matrix(temp)
    return temp

def move_left(pos,matrix):
    """ Verifica que exista un movimiento válido hacia la izquierda
    @param pos Posición vacía dentro de la matriz
    @param matrix Matriz que representa el estado actual
    return Retorna none si existe un movimiento válido o la matriz si existe
    """
    temp_matrix = matrix[:]
    temp = generate_matrix_state([pos[0],pos[1]],[pos[0],pos[1]-2],[pos[0],pos[1]-4],temp_matrix)
    #print_matrix(temp)
    return temp

def diagonal_up_right(pos,matrix):
    """ Verifica que exista un movimiento válido hacia la diagonal derecha arriba
    @param pos Posición vacía dentro de la matriz
    @param matrix Matriz que representa el estado actual
    return Retorna none si existe un movimiento válido o la matriz si existe
    """
    temp_matrix = matrix[:]
    temp = generate_matrix_state([pos[0],pos[1]],[pos[0]-1,pos[1]+1],[pos[0]-2,pos[1]+2],temp_matrix)
    #print_matrix(temp)
    return temp

def diagonal_up_left(pos,matrix):
    """ Verifica que exista un movimiento válido hacia la diagonal izquierda arriba
    @param pos Posición vacía dentro de la matriz
    @param matrix Matriz que representa el estado actual
    return Retorna none si existe un movimiento válido o la matriz si existe
    """
    temp_matrix = matrix[:]
    temp = generate_matrix_state([pos[0],pos[1]],[pos[0]-1,pos[1]-1],[pos[0]-2,pos[1]-2],temp_matrix)
    #print_matrix(temp)
    return temp

def diagonal_down_right(pos,matrix):
    """ Verifica que exista un movimiento válido hacia la diagonal derecha abajo
    @param pos Posición vacía dentro de la matriz
    @param matrix Matriz que representa el estado actual
    return Retorna none si existe un movimiento válido o la matriz si existe
    """
    temp_matrix = matrix[:]
    temp = generate_matrix_state([pos[0],pos[1]],[pos[0]+1,pos[1]+1],[pos[0]+2,pos[1]+2],temp_matrix)
    #print_matrix(temp)
    return temp

def diagonal_down_left(pos,matrix):
    """ Verifica que exista un movimiento válido hacia la diagonal izquierda abajo
    @param pos Posición vacía dentro de la matriz
    @param matrix Matriz que representa el estado actual
    return Retorna none si existe un movimiento válido o la matriz si existe
    """
    temp_matrix = matrix[:]
    temp = generate_matrix_state([pos[0],pos[1]],[pos[0]+1,pos[1]-1],[pos[0]+2,pos[1]-2],temp_matrix)
    #print_matrix(temp)
    return temp

def copiar(matrix):
    """ Hace una copia de la matriz para guardar cada uno de los estados
    @param matrix Matriz que representa el estado actual
    return copia Retorna una copia de la matriz
    """
    copia = []
    for fila in matrix:
        aux = fila.copy()
        copia.append(aux)
    return copia

def add_state(resp,list_states):
    """ Añade un nuevo estado a la lista de estados
    @param resp Respuesta que nos indica si hay un nuevo estado válido
    @param list_states Lista de estados
    """
    if(resp!=None):
        list_states.append(resp)

def get_state_for_pos(pos,matrix):
    """ Hace copias de la matriz, verifica que existan movimientos válidos y genera nuevos estados
    @param pos Posición dónde hay un espacio en la matriz que puede generar un nuevo movimiento
    @param matrix Matriz que representa el estado actual 
    return list_states Retorna la lista de estados que se generaron a partir de una posición vacía
    """
    list_states = []
    temp = copiar(matrix)
    resp = move_right(pos,temp)
    add_state(resp,list_states)
    temp = copiar(matrix)
    resp = move_left(pos,temp)
    add_state(resp,list_states)
    temp = copiar(matrix)
    resp = diagonal_up_right(pos,temp)
    add_state(resp,list_states)
    temp = copiar(matrix)
    resp = diagonal_up_left(pos,temp)
    add_state(resp,list_states)
    temp = copiar(matrix)
    resp = diagonal_down_right(pos,temp)
    add_state(resp,list_states)
    temp = copiar(matrix)
    resp = diagonal_down_left(pos,temp)
    add_state(resp,list_states)
    return list_states



def get_pos_play(matrix):
    """ Verifica las posiciones vacías que pueden generar nuevos movimientos
    @param matrix Matriz que representa el estado actual 
    return list_pos Retorna la lista de posiciones vacías de la matriz
    """
    list_pos = []
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if(matrix[i][j] == 0):
                list_pos.append([i,j])
    return list_pos

def verify_win(matrix):
    """ Verifica que el estado sea una victoria
    @param matrix Matriz que representa el estado actual 
    return Retorna 1 o 0 si el estado es final o no
    """
    num_pos=0
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if(matrix[i][j] == 1):
                num_pos+=num_pos
    if(num_pos==1):
        return num_pos
    else:
        return 0

def generate_states(matrix):
    """ Recorre las posiciones vacías de la matriz, genera los estados válidos y los movimientos para estos
    @param matrix Matriz que representa el estado actual 
    """
    print("Generando !!")
    temp = matrix[:]
    list_pos = get_pos_play(matrix)
    print(list_pos)
    for i in list_pos:
        list_states = get_state_for_pos(i,matrix)
        for w in list_states:
        	print_matrix(w)
        for j in list_states:
            if(verify_win(j)):
                break
            if j != None:
                print("############## Generate Pos #################\n")
                new_pos = get_pos_play(j)
                print(new_pos)
                for k in new_pos:
                    list_states.extend(get_state_for_pos(k,j))
        #generate_states(matrix)
    #print(list_pos)

senku_matrix = [
    [-1,-1,-1,-1, 1,-1,-1,-1,-1],
    [-1,-1,-1, 1,-1, 1,-1,-1,-1],
    [-1,-1, 1,-1, 1,-1, 1,-1,-1],
    [-1, 1,-1, 1,-1, 1,-1, 1,-1],
    [ 0,-1, 1,-1, 1,-1, 1,-1, 1],
]

list_states = []

#print(4 < len(senku_matrix))

generate_states(senku_matrix)