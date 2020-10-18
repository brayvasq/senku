from .node import Node

class Generator:
    """
    Class to represent a binary tree with the posible
    Nodes or steps to solve a senku

    ...
    Attributes
    ----------
    node : Node
        Tree root node (Initial board)

    Methods
    -------
    verify_position : bool
        Verify the board limits

    verify_values : bool
        Check if the movement can be done

    generate_state : Node
        Generates a new state
    
    right : Node
        Call for a new state by making a move to the right.

    left : Node
        Call for a new state by making a move to the left.
    
    up_right : Node
        Call for a new state by moving up to the right.

    up_left : Node
        Call for a new state by moving up to the left.

    down_right : Node
        Call for a new state by moving down to the right.
    
    down_left : Node
        Call for a new state by moving down to the left.

    copy : list
        Makes a matrix copy, avoiding to send the matrix as a reference.
    
    states : list
        Create a copy for each possible movement and ask for a new state, and add it to the possible movements.
    """

    def __init__(self, node):
        self.node = node

    def verify_position(self, target, pivot, start, matrix):
        """
        This method verifies the board limits.

        Parameters
        ----------
        target : list
            The postion of the 0 or empty position. Where the player will do the movement.

        pivot : list
            The position in middle, the item to delete

        start : list
            The position of the element to be moved.

        matrix : list
            The current board representation
        """

        # Verifiying position in X axis
        x_down  = target[1] >= 0 and pivot[1] >= 0 and start[1] >= 0
        limit_x = len(matrix[0])
        x_top   = target[1] < limit_x and pivot[1] < limit_x and start[1] < limit_x

        # Verifiying position in Y axis
        y_down  = target[0] >= 0 and pivot[0] >= 0 and start[0] >= 0
        limit_y = len(matrix)
        y_top   = target[0] < limit_y and pivot[0] < limit_y and start[0] < limit_y

        return x_down and x_top and y_down and y_top

    def verify_values(self, target, pivot, start, matrix):
        """
        Check if the movement can be done. A movement is correct if:
            Start value = 1
            Pivot value = 1
            Target valye = 0

        Parameters
        ----------
        target : list
            The postion of the 0 or empty position. Where the player will do the movement.

        pivot : list
            The position in middle, the item to delete

        start : list
            The position of the element to be moved.

        matrix : list
            The current board representation
        """
        return matrix[target[0]][target[1]] == "0" and matrix[pivot[0]][pivot[1]] == "1" and matrix[start[0]][start[1]] == "1"

    def generate_state(self, target, pivot, start, matrix):
        """
        Generates a new state. Doing the movement given by the target, pivot and start parameters

        Parameters
        ----------
        target : list
            The postion of the 0 or empty position. Where the player will do the movement.

        pivot : list
            The position in middle, the item to delete

        start : list
            The position of the element to be moved.

        matrix : list
            The current board representation
        """
        resp = None

        if self.verify_position(target, pivot, start, matrix) and self.verify_values(target, pivot, start, matrix):
            matrix[target[0]][target[1]] = "1"
            matrix[pivot[0]][pivot[1]] = "0"
            matrix[start[0]][start[1]] = "0"
            resp = matrix

        return resp

    def right(self, position, matrix):
        """
        Call for a new state by making a move to the right.
            0                0
           0 0              0 0
          0 0 0     -->    0 0 0
         0 0 0 0          0 0 0 0
        1 1 0 0 0        0 0 1 0 0

        Parameters
        ----------
        position : str
            The position of the element to be moved.
              position[0] --> Y Axis
              position[1] --> X Axis

        matrix : list
            The current board representation
        """
        state = self.generate_state([position[0], position[1]], [position[0], position[1] + 2], [position[0], position[1] + 4], matrix)
        return Node(state) if state is not None else None

    def left(self, position, matrix):
        """
        Call for a new state by making a move to the left.
            0                0
           0 0              0 0
          0 0 0     -->    0 0 0
         0 0 0 0          0 0 0 0
        0 1 1 0 0        1 0 0 0 0

        Parameters
        ----------
        position : str
            The position of the element to be moved.
              position[0] --> Y Axis
              position[1] --> X Axis

        matrix : list
            The current board representation
        """
        state = self.generate_state([position[0], position[1]], [position[0], position[1] - 2], [position[0], position[1] - 4], matrix)
        return Node(state) if state is not None else None

    def up_right(self, position, matrix):
        """
        Call for a new state by moving up to the right.
            0                0
           0 0              0 0
          0 0 0     -->    0 1 0
         0 1 0 0          0 0 0 0
        0 1 0 0 0        0 0 0 0 0

        Parameters
        ----------
        position : str
            The position of the element to be moved.
              position[0] --> Y Axis
              position[1] --> X Axis

        matrix : list
            The current board representation
        """
        state = self.generate_state([position[0], position[1]], [position[0] - 1, position[1] + 1], [position[0] - 2, position[1] + 2], matrix)
        return Node(state) if state is not None else None

    def up_left(self, position, matrix):
        """
        Call for a new state by moving up to the left.
            0                0
           0 0              0 0
          0 0 0     -->    1 0 0
         0 1 0 0          0 0 0 0
        0 0 1 0 0        0 0 0 0 0

        Parameters
        ----------
        position : str
            The position of the element to be moved.
              position[0] --> Y Axis
              position[1] --> X Axis

        matrix : list
            The current board representation
        """
        state = self.generate_state([position[0], position[1]], [position[0] - 1, position[1] - 1], [position[0] - 2, position[1] - 2], matrix)
        return Node(state) if state is not None else None

    def down_right(self, position, matrix):
        """
        Call for a new state by moving down to the right.
            0                0
           0 0              0 0
          1 0 0     -->    0 0 0
         0 1 0 0          0 0 0 0
        0 0 0 0 0        0 0 1 0 0

        Parameters
        ----------
        position : str
            The position of the element to be moved.
              position[0] --> Y Axis
              position[1] --> X Axis

        matrix : list
            The current board representation
        """
        state = self.generate_state([position[0], position[1]], [position[0] + 1, position[1] + 1], [position[0] + 2, position[1] + 2], matrix)
        return Node(state) if state is not None else None

    def down_left(self, position, matrix):
        """
        Call for a new state by moving down to the left.
            0                0
           0 1              0 0
          0 1 0     -->    0 0 0
         0 0 0 0          0 1 0 0
        0 0 0 0 0        0 0 0 0 0

        Parameters
        ----------
        position : str
            The position of the element to be moved.
              position[0] --> Y Axis
              position[1] --> X Axis

        matrix : list
            The current board representation
        """
        state = self.generate_state([position[0], position[1]], [position[0] + 1, position[1] - 1], [position[0] + 2, position[1] - 2], matrix)
        return Node(state) if state is not None else None

    def copy(self, matrix):
        """
        Makes a matrix copy, avoiding to send the matrix as a reference.

        matrix : str
            The current board representation
        """
        temp = []

        for i in matrix:
            aux = i.copy()
            temp.append(aux)
        
        return temp

    def states(self, node, position):
        """
        Create a copy for each possible movement and ask for a new state, and add it to the possible movements.

        Parameters
        ----------
        node : Node
            The current node.
        
        position : list
            The position of the node.
        """
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
