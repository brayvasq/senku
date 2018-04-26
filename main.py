def verify_pos(start,middle,end,matrix):
    pos_x_down = start[1] >= 0 and middle[1] >= 0 and end[1] >= 0
    pos_x_top = start[1] < len(matrix[0]) and middle[1] < len(matrix[0]) and end[1] < len(matrix[0])

    pos_y_down = start[0] >= 0 and middle[0] >= 0 and end[0] >= 0
    pos_y_top = start[0] < len(matrix) and middle[0] < len(matrix) and end[0] < len(matrix)

    return pos_x_down and pos_x_top and pos_y_down and pos_y_top

def verify_vals(start,middle,end,matrix):
    return matrix[start[0]][start[1]] == 0 and matrix[middle[0]][middle[1]] == 1 and matrix[end[0]][end[1]] == 1

def print_matrix(matrix):
    if(matrix!=None):
        for i in matrix:
            print(i)
        print("\n")

def generate_matrix_state(start,middle,end,matrix):
    resp = None
    if(verify_pos(start,middle,end,matrix) and verify_vals(start,middle,end,matrix)):
        matrix[start[0]][start[1]] = 1
        matrix[middle[0]][middle[1]] = 0
        matrix[end[0]][end[1]] = 0
        resp = matrix
    return resp

def move_right(pos,matrix):
    temp_matrix = matrix[:]
    temp = generate_matrix_state([pos[0],pos[1]],[pos[0],pos[1]+2],[pos[0],pos[1]+4],temp_matrix)
    print_matrix(temp)
    return temp

def move_left(pos,matrix):
    temp_matrix = matrix[:]
    temp = generate_matrix_state([pos[0],pos[1]],[pos[0],pos[1]-2],[pos[0],pos[1]-4],temp_matrix)
    print_matrix(temp)
    return temp

def diagonal_up_right(pos,matrix):
    temp_matrix = matrix[:]
    temp = generate_matrix_state([pos[0],pos[1]],[pos[0]-1,pos[1]+1],[pos[0]-2,pos[1]+2],temp_matrix)
    print_matrix(temp)
    return temp

def diagonal_up_left(pos,matrix):
    temp_matrix = matrix[:]
    temp = generate_matrix_state([pos[0],pos[1]],[pos[0]-1,pos[1]-1],[pos[0]-2,pos[1]-2],temp_matrix)
    print_matrix(temp)
    return temp

def diagonal_down_right(pos,matrix):
    temp_matrix = matrix[:]
    temp = generate_matrix_state([pos[0],pos[1]],[pos[0]+1,pos[1]+1],[pos[0]+2,pos[1]+2],temp_matrix)
    print_matrix(temp)
    return temp

def diagonal_down_left(pos,matrix):
    temp_matrix = matrix[:]
    temp = generate_matrix_state([pos[0],pos[1]],[pos[0]+1,pos[1]-1],[pos[0]+2,pos[1]-2],temp_matrix)
    print_matrix(temp)
    return temp

def copiar(matrix):
    copia = []
    for fila in matrix:
        aux = fila.copy()
        copia.append(aux)
    return copia

def add_state(resp,list_states):
    if(resp!=None):
        list_states.append(resp)

def get_state_for_pos(pos,matrix):
    list_states = []
    temp = copiar(matrix)
    resp = move_right(pos,temp)
    add_state(resp,list_states)
    temp = copiar(matrix)
    resp = move_right(pos,temp)
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
    list_pos = []
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if(matrix[i][j] == 0):
                list_pos.append([i,j])
    return list_pos

def generate_states(matrix):
    print("Generando !!")
    temp = matrix[:]
    list_pos = get_pos_play(matrix)
    for i in list_pos:
        list_states = get_state_for_pos(i,matrix)
        print(list_states)
        for j in list_states:
            if j != None:
                print("############## Generate Pos #################\n")
                new_pos = get_pos_play(j)
                print(new_pos)
                for k in new_pos:
                    get_state_for_pos(k,j)
    

        #generate_states(matrix)
    #print(list_pos)

senku_matrix = [
    [-1,-1,-1,-1, 1,-1,-1,-1,-1],
    [-1,-1,-1, 1,-1, 1,-1,-1,-1],
    [-1,-1, 1,-1, 0,-1, 1,-1,-1],
    [-1, 1,-1, 1,-1, 1,-1, 1,-1],
    [ 1,-1, 1,-1, 1,-1, 1,-1, 1],
]

list_states = []

#print(4 < len(senku_matrix))

generate_states(senku_matrix)