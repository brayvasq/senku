# Senku Game
Senku game solver.

| Lenguaje | Versión        | SO                      |
| -------- | -------------- | -----------------       |
| Python   | Python 3.8.2   | Ubuntu 20.04            |


## Run project
```bash
# Setup environment
virtualenv venv
source venv/bin/activate

# Installing dependencies
pip install -r requirements.txt

# Run project
python main.py
```
## Usage
### Solve command
```bash
python main.py solve
python main.py s

Senku solver - A simple Senku solver

Usage:
  python main.py [command]
or if you want to take times
  time python main.py [command]

Available Commands:
  [solve   | s]   <name=>            solve the senku game using the given algorithm
  [help    | h]                      help about commands


Examples:
  BFS Algorithm: Breadth First Search
    python main.py solve name=bfs

  DFS Algorithm: Depth First Search
    python main.py solve name=dfs

  Greedy Algorithm
    python main.py solve name=greedy

  A*: A Star
    python main.py solve name=astar
```

## Pending
- [ ] Document code.
- [ ] Document algorithms in `NOTES.md`.
- [ ] Document senku game theory in `NOTES.md`.
- [ ] Add unit tests.
- [ ] Migrate to a web project (Django or Flask).
- [ ] Add other versions of senku.
