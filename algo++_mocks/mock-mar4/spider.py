UP = "U"
DOWN = "D"

distances = [3, 2, 5, 3, 1, 2]

class Solver():
    def __init__(self):
        self.start = 0
        self.current = 0
        self.goal = 0
        self.solution = None

    # Returns all possible (state,action) from current node
    def actions(self, current_total):
        result = []
        moves = [UP, DOWN] # Follows order in handout
        for m in moves:
            if m == UP:
                result.append((m, current_total+next))
            else:
                result.append((m, current_total-next))
            # if validateMove(state, m):
            #     result.append((m, move(deepcopy(state), m)))
        return result

    # Get x, y positions of given tile value in the goal state
    def get_goal_position(self, tile):
        for x in range(3):
            for y in range(3):
                if self.goal[x][y] == tile:
                    return x, y

    # Find h(n)
    def find_h(self, board):
        # Sum of all computed manhattan distance
        h = 0
        # Go through each tile of the state and get its manhattan distance
        for x2 in range(3):
            for y2 in range(3):
                # Don't count the empty tile
                if board[x2][y2] != 0:
                    # Find position of tile in the goal state
                    x1, y1 = self.get_goal_position(board[x2][y2])
                    # Manhattan distance = | x1 - x2 | + | y1 - y2 |
                    h += abs(x1 - x2) + abs(y1 - y2)

        return h

    # Solver
    def solve(self, algo):
        print("Solving...")
        
        # Initialize
        start = Node(state=self.start, parent=None, action=None, g=0, h=0)
        if algo == "DFS":
            frontier = DFS_Frontier()
        elif algo == "BFS":
            frontier = BFS_Frontier()
        elif algo == "A*":
            frontier = AStar_Frontier()
        frontier.add(start)

        self.explored = set()

        # Keep exploring new states until found goal state
        while True:
            if frontier.empty():
                print("Empty frontier, unsolvable.")
                pygame.quit()
                sys.exit()
            
            # Mark node as explored
            node = frontier.remove()
            self.explored.add(str(node.state)) # set() does not accept lists; need to stringify entries

            # When found goal state, store solution
            if node.state == self.goal:
                solution = []

                # "Crawl" back to find solution
                while node.parent is not None:
                    solution.append(node.action)
                    node = node.parent
                solution.reverse()

                # Write to puzzle.out
                f = open('puzzle.out', 'w')
                f.write(" ".join(solution))
                f.close()

                print("Solution: " + ", ".join(list(map(lambda move: move, solution))))
                print("Path cost of solution: " + str(len(solution)))
                print("Number of paths explored to find solution: " + str(len(self.explored)))
                return

            # Go through action space and explore each action
            for action, state in self.actions(node.state):
                if not frontier.contains_state(state) and str(state) not in self.explored:
                    child = Node(state=state, parent=node, action=action, g=node.g+1, h=self.find_h(state))
                    frontier.add(child)
                    print(state)

n = int(input(""))
for i in range(n):
    m = int(input(""))
    distances = list(map(lambda x: int(x), input().split(" ")))