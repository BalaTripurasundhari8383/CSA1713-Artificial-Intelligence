from collections import deque

def is_goal(state, target):
    return state[0] == target or state[1] == target

def bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()
    parent = {}
    goal_reached = None

    start = (0, 0)
    queue.append(start)
    visited.add(start)

    # First Phase: Reach target (2 gallons)
    while queue:
        jug1, jug2 = queue.popleft()

        if is_goal((jug1, jug2), target):
            goal_reached = (jug1, jug2)
            break

        possible_moves = [
            (jug1_capacity, jug2),
            (jug1, jug2_capacity),
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1)),
        ]

        for state in possible_moves:
            if state not in visited:
                visited.add(state)
                parent[state] = (jug1, jug2)
                queue.append(state)

    if not goal_reached:
        return None

    # Reconstruct path to reach 2 gallons
    path = [goal_reached]
    current = goal_reached
    while current in parent:
        current = parent[current]
        path.append(current)
    path.reverse()

    # Second Phase: Go back to (0, 0)
    queue = deque()
    visited = set()
    parent = {}

    queue.append(goal_reached)
    visited.add(goal_reached)

    end_state = (0, 0)

    while queue:
        jug1, jug2 = queue.popleft()

        if (jug1, jug2) == end_state:
            backtrack = [(jug1, jug2)]
            while (jug1, jug2) in parent:
                jug1, jug2 = parent[(jug1, jug2)]
                backtrack.append((jug1, jug2))
            backtrack.reverse()
            path.extend(backtrack[1:])  # avoid repeating the mid-point
            return path

        possible_moves = [
            (jug1_capacity, jug2),
            (jug1, jug2_capacity),
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1)),
        ]

        for state in possible_moves:
            if state not in visited:
                visited.add(state)
                parent[state] = (jug1, jug2)
                queue.append(state)

    return path

# Settings
jug1 = 3
jug2 = 4
target = 2

result = bfs(jug1, jug2, target)

if result:
    print("Steps to reach 2 gallons and return to empty:")
    for step in result:
        print(f"Jug1: {step[0]} gallons, Jug2: {step[1]} gallons")
else:
    print("No solution found.")
