from .generator import Generator
from .node import Node
from .algorithm import Algorithm

class AStar(Algorithm):
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

            node = frontier[0]
            node.step = steps
            node.name = f"Node: {str(node.step)}"
            # TODO: review if it returns the node in that position
            # to attach it directly to node var
            frontier.pop(0)

            if not list(visited.values()).__contains__(node):
                visited[node.step] = node

            childs = self.neighbors(node, list(visited.values()), frontier)
            
            for i in childs:
                i.parent_id = node.step

            if(node.verify_winner()):
                search = False

            for i in childs:
                n = i.count_pegs() # Number of filled items
                childs = self.neighbors(i, list(visited.values()), frontier)
                i.heuristic = n - ((1 / n) * len(childs))
                frontier.append(i)

            frontier = self.sort_by_heuristic(frontier)
        
        print(f"Steps: {steps}")
        return self.path(node, visited, steps)

    def sort_by_heuristic(self, frontier):
        return sorted(frontier, key=lambda node: node.heuristic)

    # TODO: Move to the parent class
    def path(self, node, visited, steps):
        parent = node.step
        track = []
        print(type(visited))

        while(parent > 1):
            temp = visited[parent]
            track.append(temp)
            parent = temp.parent_id

        # Reverse the list
        track = track[::-1]
        solution_steps = len(track)
        print(solution_steps)

        print(node)
        for i in track:
            print(i)

        return track, steps, solution_steps



