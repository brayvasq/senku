class Node:
    """
    Class that represent a tile or node in a senku game.

    ...
    Attributes
    ----------
    step : int
        The step or node geneared
    parent_id : int
        The Node parent id
    name : str
        Node name
    matrix : list
        The matrix representation.
    level : int
        The level in senku, is equivalent to the number of movements
    parent : Node
        The node parent
    heuristic : int
        A value that tell us how near is the node to a solution
    
    Methods
    -------
    count_pegs : int
        Counts the number of filled items.

    count_level : int
        Counts the number of empty items.

    positions_to_play : list
        Look for possible movements

    verify_winner : bool
        Check if the Node is a solution   

    tiles : str
        Returns the string representation for a row

    
    """

    def __init__(self, matrix):
        """
        Parameters
        ----------
        matrix : list
            The matrix representation.
        """
        self.step = 0
        self.parent_id = 0
        self.name = f'Node: {str(self.step)}!'
        self.matrix = matrix
        self.level = 0
        self.parent = None
        self.heuristic = 0

    def count_pegs(self):
        """
        Counts the number of filled items (equals to 1).

        Return
        ------
            The number of filled items
        """
        count = 0

        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if self.matrix[i][j] == "1":
                    count += 1

        return count

    def count_level(self):
        """
        Counts the number of empty items (equals to 0).
        The level is the number of movements made.

        Return
        ------
            The number of empty items
        """
        count = 0

        for i in range(0, len(self.matrix)):
            for j in range(0,len(self.matrix[i])):
                if self.matrix[i][j] == "0":
                    count += 1

        # We substract 1 to count level from 0
        return count - 1

    def positions_to_play(self):
        """
        Look for target positions and put them into a list
        
        Return 
        ------
            a list of target positions
        """

        positions = []

        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if self.matrix[i][j] == "0":
                    # Add [row, column] to the list
                    positions.append([i, j])
        
        return positions

    def verify_winner(self):
        """
        Check if the Node is a solution

        Return
        ------
            true if the Node is solution
        """
        return self.count_pegs() == 1

    def tiles(self, nums, row = 1, spaces = 0):
        """
        Returns the string representation for a row
        to be printed

        ...
        Parameters
        ----------
        nums : list
            An array with the tiles values

        row : int
            The row number

        spaces : int
            The number of spaces to add to the string.

        Return
        ------
            A string with the rows values formated
        """
        # We add the (" " * 5) to align the rows
        # with odd number of values
        separator = ("+---+" + (" " * 5)) * row
        space = (" " * 5) * spaces

        tile  = space + separator  + space + "\n"
        
        tile += space
        for i in nums:
            # We add the (" " * 5) to align the rows
            # with odd number of values
            tile += f"| {i} |" + (" " * 5)
        tile += space + "\n"
        
        tile += space + separator  + space + "\n"
        
        return tile

    def __str__(self):
        """
        Iterates the Node matrix and return the string 
        that represents the Node

        Return
        ------
            Node representative string
        """
        # The full representative string
        str_matrix = ""

        if self.matrix is not None:
            # Save the lenght into a variable
            # to send this number to the tiles method
            # and calculate the number of spaces
            spaces = len(self.matrix)
            for i in range(0, spaces):
                nums = list(filter(lambda x: x != "_", self.matrix[i]))
                str_matrix += self.tiles(nums, (i+1), (spaces - i))

        return str_matrix

    def __eq__(self, other):
        """
        Compares two Nodes.

        Parameters
        ----------
        other : Node
            Element to be compared

        Return
        ------
            true if both Nodes have the same matrix
        """
        return self.matrix == other.matrix
