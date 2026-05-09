import heapq

# Goal State
goal_state = [[1,2,3],[4,5,6],[7,8,0]]

# Node class
class Node:
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val - 1) // 3
                goal_y = (val - 1) % 3
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def a_star(start_state):
    open_list = []
    closed_set = set()

    start_node = Node(start_state, None, 0, heuristic(start_state))
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.state == goal_state:
            return reconstruct_path(current)

        closed_set.add(str(current.state))

        for neighbor in get_neighbors(current.state):
            if str(neighbor) in closed_set:
                continue

            g = current.g + 1
            h = heuristic(neighbor)

            neighbor_node = Node(neighbor, current, g, h)
            heapq.heappush(open_list, neighbor_node)

    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

start = []
for i in range(3) :
    my_lst = list(map(lambda x : int(x),input(f"Please enter row no. {i} in (space separated values) : ").split()))
    start.append(my_lst)
    
solution = a_star(start)

if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")
