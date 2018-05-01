class Node:
    """
        :version: 0.1
        This is a simple class that represent a node for a "senku" game solve
    """

    def __init__(self,matrix):
        """
            This method is a constructor of the class

            :param: matrix is the representation of the "senku" game state
            :param: step is the number in which the state was generated

            :return: nothing
        """
        self.step   = 0
        self.name   = "Node : "+str(self.step)
        self.matrix = matrix
        self.parent = None
    
    def print_info(self):
        """
            This method show a simple name for her.

            :params: nothing

            :return: nothing
        """
        print(self.name)

    def print_matrix(self):
        """
            This method iterate the matrix and show her like a 
            triangle "senku" matrix.

            :param: matrix, representation of the "senku" game state

            :return: nothing
        """
        string_matrix = "";
        if self.matrix != None:
            for i in range(0,len(self.matrix)):
                for j in range(0,len(self.matrix[i])):
                    if self.matrix[i][j] != -1 :
                        string_matrix += " " + str(self.matrix[i][j]) + " "
                    else:
                        string_matrix += "   "
                string_matrix += "\n"
            print(string_matrix)

    def __str__(self):
        return self.name

    def __eq__(self,other):
        return self.matrix == other.matrix

    
