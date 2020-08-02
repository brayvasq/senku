from .generator import Generator
from .node import Node
from .algorithm import Algorithm

class DFS(Algorithm):
    def __init__(self, node):
        Algorithm.__init__(self, node)

    def run(self):
        search = True
        steps = 0

        temp = self.generator.copy(self.root.matrix[:])
        state = Node(temp)
        frontier = [state]
        visited  = {}

        while search and len(frontier) > 0:
            steps += 1

            node = frontier[len(frontier)-1]
            node.step = steps
            node.name = f"Node: {str(node.step)}"
            # TODO: review if it returns the node in that position
            # to attach it directly to node var
            frontier.pop(len(frontier) - 1)

            if not list(visited.values()).__contains__(node):
                visited[node.step] = node

            childs = self.neighbors(node, list(visited.values()), frontier)
            
            for i in childs:
                i.parent_id = node.step

            if(node.verify_winner()):
                search = False

            for i in childs:
                frontier.append(i)

        print(steps)
        return self.path(node, visited)

    # TODO: Move to the parent class
    def path(self, node, visited):
        parent = node.step
        track = []

        while parent > 1:
            temp = visited[parent]
            track.append(temp)
            parent = temp.parent_id
            
        track = track[::-1]
        print(len(track))

        print(node)
        for i in track:
            print(i)

        return track
