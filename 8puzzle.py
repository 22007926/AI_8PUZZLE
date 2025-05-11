from collections import deque
import heapq

# Initial and Goal States
initial_state = [
    [1, 8, 2],
    [4, 0, 3],
    [7, 6, 5]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Helper Functions
def get_point(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)
    return (0, 0)

def get_state(state):
    new_states = []
    x, y = get_point(state)
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            temp = [row[:] for row in state]
            temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y]
            new_states.append(temp)
    return new_states

def serial(state):
    return tuple(tuple(row) for row in state)

def display(path):
    if path is None:
        print("No solution found.\n")
        return
    for i, state in enumerate(path):
        print(f"Step {i}:")
        for row in state:
            print(row)
        print()

# BFS
def bfs(first_state):
    q = deque([(first_state, [first_state])])
    vis = set()
    vis.add(serial(first_state))
    
    while q:
        state, path = q.popleft()
        if state == goal_state:
            return path
        for new_state in get_state(state):
            s = serial(new_state)
            if s not in vis:
                vis.add(s)
                q.append((new_state, path + [new_state]))
    return None

# DFS with Depth Limit
def dfs(first_state, depth_limit=20):
    stack = deque([(first_state, [first_state], 0)])
    vis = set()
    vis.add(serial(first_state))

    while stack:
        state, path, depth = stack.pop()
        if state == goal_state:
            return path
        if depth < depth_limit:
            for new_state in get_state(state):
                s = serial(new_state)
                if s not in vis:
                    vis.add(s)
                    stack.append((new_state, path + [new_state], depth + 1))
    return None

# Manhattan Distance for A*
def manhattan_distance(state):
    distance = 0
    goal_positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1)
    }
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_i, goal_j = goal_positions[val]
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# A* Search
def a_star(first_state):
    pq = []
    heapq.heappush(pq, (manhattan_distance(first_state), 0, first_state, [first_state]))
    vis = set()
    vis.add(serial(first_state))

    while pq:
        est_total, cost, state, path = heapq.heappop(pq)
        if state == goal_state:
            return path
        for new_state in get_state(state):
            s = serial(new_state)
            if s not in vis:
                vis.add(s)
                new_cost = cost + 1
                est = new_cost + manhattan_distance(new_state)
                heapq.heappush(pq, (est, new_cost, new_state, path + [new_state]))
    return None

# Menu System
while True:
    print("\nSelect the algorithm to solve the 8-Puzzle:")
    print("1. Breadth-First Search (BFS)")
    print("2. Depth-First Search (DFS)")
    print("3. A* Search")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\nBFS Solution:")
        display(bfs(initial_state))
    elif choice == "2":
        print("\nDFS Solution:")
        display(dfs(initial_state, depth_limit=20))
    elif choice == "3":
        print("\nA* Solution:")
        display(a_star(initial_state))
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
