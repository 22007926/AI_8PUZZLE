from collections import deque
import heapq

# ----------------------------------------
# Initial and Goal States of the 8-puzzle
# ----------------------------------------

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

# ----------------------------------------
# Helper Functions
# ----------------------------------------

def get_point(state):
    """Finds the coordinates of the blank tile (0) in the current puzzle state."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)
    return (0, 0)

def get_state(state):
    """
    Generates all possible next states by sliding the blank tile
    in all 4 possible directions (if valid).
    """
    new_states = []
    x, y = get_point(state)

    # Moves: (Up, Down, Left, Right)
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            temp = [row[:] for row in state]  # Deep copy
            # Swap blank tile with the adjacent tile
            temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y]
            new_states.append(temp)
    return new_states

def serial(first_state):
    """Converts a 2D list state to a hashable tuple for use in sets."""
    return tuple(tuple(row) for row in first_state)

def display(path):
    """Displays the sequence of states from the initial to goal."""
    if path is None:
        print("No solution found.\n")
        return
    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()

# ----------------------------------------
# Search Algorithms
# ----------------------------------------

def bfs(first_state):
    """Breadth-First Search algorithm (BFS) implementation."""
    # Queue stores tuples of (current_state, path_to_state)
    queue = deque([(first_state, [first_state])])
    visited = {serial(first_state)}

    while queue:
        current_state, path = queue.popleft()

        # BFS GOAL CHECK
        if current_state == goal_state:
            return path

        for next_state in get_state(current_state):
            if serial(next_state) not in visited:
                visited.add(serial(next_state))
                queue.append((next_state, path + [next_state]))

    return None  # No solution found

def dfs(first_state, depth_limit=50):
    """Depth-First Search algorithm (DFS) with a depth limit."""
    # Stack stores tuples of (current_state, path_to_state)
    stack = [(first_state, [first_state])]
    visited = {serial(first_state)}

    while stack:
        current_state, path = stack.pop()

        # DFS GOAL CHECK
        if current_state == goal_state:
            return path

        if len(path) < depth_limit:
            # Explore deeper first
            for next_state in reversed(get_state(current_state)):
                if serial(next_state) not in visited:
                    visited.add(serial(next_state))
                    stack.append((next_state, path + [next_state]))

    return None  # No solution found

def manhattan_distance(state):
    """Heuristic: Calculates Manhattan distance between current state and goal state."""
    distance = 0
    goal_positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 0: (2, 2)
    }

    for i in range(3):
        for j in range(3):
            value = state[i][j]
            goal_i, goal_j = goal_positions[value]
            distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def a_star(first_state):
    """
    A* Search algorithm using the Manhattan distance heuristic.
    f(n) = g(n) + h(n)
    where g(n) is the cost to reach current state,
    and h(n) is estimated cost to goal (Manhattan distance).
    """
    # Priority Queue stores: (f_score, g_score, current_state, path)
    priority_queue = [(manhattan_distance(first_state), 0, first_state, [first_state])]
    visited = {serial(first_state)}

    while priority_queue:
        f_score, g_score, current_state, path = heapq.heappop(priority_queue)

        # A* GOAL CHECK
        if current_state == goal_state:
            return path

        for next_state in get_state(current_state):
            if serial(next_state) not in visited:
                visited.add(serial(next_state))
                new_g_score = g_score + 1
                h_score = manhattan_distance(next_state)
                new_f_score = new_g_score + h_score
                heapq.heappush(priority_queue, (new_f_score, new_g_score, next_state, path + [next_state]))

    return None  # No solution found

# ----------------------------------------
# Menu-Driven Interface
# ----------------------------------------

while True:
    print("\nSelect the algorithm to solve the 8-Puzzle:")
    print("1. Breadth-First Search (BFS)")
    print("2. Depth-First Search (DFS)")
    print("3. A* Search")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\n--- BFS Solution ---")
        display(bfs(initial_state))  # BFS is called here
    elif choice == "2":
        print("\n--- DFS Solution ---")
        display(dfs(initial_state))  # DFS is called here
    elif choice == "3":
        print("\n--- A* Search Solution ---")
        display(a_star(initial_state))  # A* is called here
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
