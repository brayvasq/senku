import re
from .game import Game

class Commands:
    def __init__(self, data):
        self.game = Game()
        self.data = data
        self.size = len(data)

    def process(self):
        command = self.__command()

        if command:
            self.__run_command(command)
        else:
            self.__help()

    def __command(self):
        command = None

        if self.size > 1:
            command = self.data[1]
        
        return command

    def __run_command(self, command):
        if command in ["solve", "s"]:
            self.__solve_command()
        elif command in ["help", "h"]:
            self.__help()
        else:
            self.__help()

    def __solve_command(self):
        name = self.__param("name=", "([a-zA-Z]+)")

        if name:
            self.game.process(name)
        else:
            print("Error!: A name is required to run the project")
            self.__help()


    def __param(self, param, pattern):
        """
        Returns the queried param using regex
        Parameters
        ----------
        param : str
            variable name to search
        pattern : str
            variable pattern equivalent
        Return
        ------
        value : str
            the param value if a match occurs
        None
            otherwise
        """
        value = None

        if self.size > 2:
            data_str = ';'.join(self.data[2:])
            value = re.search(param + pattern, data_str)
            if value:
                value = value.group(1).replace(param, '') if value.group(1) else None

        return value
    
    def __help(self):
        """
        Shows help for the app
        Return
        ------
        None
        """
        print("Senku solver - A simple Senku solver")
        print()
        print("Usage:")
        print("  python main.py [command]")
        print("or if you want to take times")
        print("  time python main.py [command]")
        print()
        print("Available Commands:")
        print("  [solve   | s]   <name=>            solve the senku game using the given algorithm")
        print("  [help    | h]                      help about commands")
        print()
        print("")
        print("Examples:")
        print("  BFS Algorithm: Breadth First Search")
        print("    python main.py solve name=bfs")
        print()
        print("  DFS Algorithm: Depth First Search")
        print("    python main.py solve name=dfs")
        print()
        print("  Greedy Algorithm")
        print("    python main.py solve name=greedy")
        print()
        print("  A*: A Star")
        print("    python main.py solve name=astar")
