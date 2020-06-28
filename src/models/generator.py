from src.models.node import Node

class Generator:
    """
    Class to represent a binary tree with the posible
    Nodes or steps to solve a senku

    ...
    Attributes
    ----------
    """

    def __init__(self, node):
        self.node = node # Initial Node

    def verify_position(self, target, pivot, start, matrix):
        # This method verifies the board limits
        # Verifiying position in X axis
        # Target is the postion of the 0  or empty position
        x_down  = target[1] >= 0 and pivot[1] >= 0 and start[1] >= 0
        limit_x = len(matrix[0])
        x_top   = target[1] < limit_x and pivot[1] < limit_x and start[1] < limit_x

        # Verifiying position in Y axis
        y_down  = target[0] >= 0 and pivot[0] >= 0 and start[0] >= 0
        limit_y = len(matrix)
        y_top   = target[0] < limit_y and pivot[0] < limit_y and start[0] < limit_y

        return x_down and x_top and y_down and y_top

    def verify_values(self, target, pivot, start, matrix):
        return matrix[target[0]][target[1]] == "0" and matrix[pivot[0]][pivot[1]] == "1" and matrix[start[0]][start[1]] == "1"

    def generate_state(self, target, pivot, start, matrix):
        # This method generate a single state
        resp = None

        if self.verify_position(target, pivot, start, matrix) and self.verify_values(target, pivot, start, matrix):
            matrix[target[0]][target[1]] = "1"
            matrix[pivot[0]][pivot[1]] = "0"
            matrix[start[0]][start[1]] = "0"
            resp = matrix

        return resp

    def right(self, position, matrix):
        # This method moves rigth
        # pos[0] - X
        # pos[1] - Y
        state = self.generate_state([position[0], position[1]], [position[0], position[1] + 2], [position[0], position[1] + 4], matrix)
        return Node(state) if state is not None else None

    def left(self, position, matrix):
        state = self.generate_state([position[0], position[1]], [position[0], position[1] - 2], [position[0], position[1] - 4], matrix)
        return Node(state) if state is not None else None

    def up_right(self, position, matrix):
        state = self.generate_state([position[0], position[1]], [position[0] - 1, position[1] + 1], [position[0] - 2, position[1] + 2], matrix)
        return Node(state) if state is not None else None

    def up_left(self, position, matrix):
        state = self.generate_state([position[0], position[1]], [position[0] - 1, position[1] - 1], [position[0] - 2, position[1] - 2], matrix)
        return Node(state) if state is not None else None

    def down_right(self, position, matrix):
        state = self.generate_state([position[0], position[1]], [position[0] + 1, position[1] + 1], [position[0] + 2, position[1] + 2], matrix)
        return Node(state) if state is not None else None

    def down_left(self, position, matrix):
        state = self.generate_state([position[0], position[1]], [position[0] + 1, position[1] - 1], [position[0] + 2, position[1] - 2], matrix)
        return Node(state) if state is not None else None

    def copy(self, matrix):
        temp = []

        for i in matrix:
            aux = i.copy()
            temp.append(aux)
        
        return temp

    def states(self, node, position):
        # This method generates the states
        movements = []

        temp = self.copy(node.matrix[:])
        state = self.right(position, temp)

        if state is not None:
            movements.append(state)

        temp = self.copy(node.matrix[:])
        state = self.left(position, temp)

        if state is not None:
            movements.append(state)

        temp = self.copy(node.matrix[:])
        state = self.up_right(position, temp)

        if state is not None:
            movements.append(state)

        temp = self.copy(node.matrix[:])
        state = self.up_left(position, temp)

        if state is not None:
            movements.append(state)

        temp = self.copy(node.matrix[:])
        state = self.down_right(position, temp)

        if state is not None:
            movements.append(state)

        temp = self.copy(node.matrix[:])
        state = self.down_left(position, temp)

        if state is not None:
            movements.append(state)

        return movements
