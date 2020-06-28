from src.models.generator import Generator
from src.models.node import Node

class Algorithm:
    def __init__(self, root):
        self.root = root
        self.generator = Generator(self.root)

    # neighbors: Child nodes
    def find_winner(self, neighbors):
        winner = False

        if(neighbors != None):
            for i in neighbors:
                resp = i.verify_winner()
                if resp:
                    break
    
        return resp

    # node: item from which we will get neighbors
    # visited: visited nodes
    # frontier: nodes that we will visit, to avoid to repeat states
    #           and create cycles
    def neighbors(self, node, visited, frontier):
        positions = node.positions_to_play()

        childs = []

        for position in positions:
            states = self.generator.states(node, position)
 
            for state in states:
                #if (not childs.__contains__(state)) and (not visited.__contains__(state)) and (not frontier.__contains__(node)):
                if (not any(x.matrix == state.matrix for x in childs)) and (not any(x.matrix == state.matrix for x in visited)) and (not any(x.matrix == state.matrix for x in frontier)):
                    childs.append(state)

        return childs

    def run():
        pass

    def path():
        pass

