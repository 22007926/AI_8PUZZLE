from collections import deque

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

if __name__ == "__main__":
    print("Solving 8-Puzzle using Depth-First Search (Depth Limit = 20):")
    solution = dfs(initial_state, depth_limit=20)
    display(solution)
