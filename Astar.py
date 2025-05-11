import heapq

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

if __name__ == "__main__":
    print("Solving 8-Puzzle using A* Search with Manhattan Distance:")
    solution = a_star(initial_state)
    display(solution)
