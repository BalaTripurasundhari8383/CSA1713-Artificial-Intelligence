from collections import deque

class State:
    def __init__(self, missionaries_left, cannibals_left, boat_left, path=[]):
        self.m = missionaries_left
        self.c = cannibals_left
        self.b = boat_left  # 1 if boat is on left, 0 if on right
        self.path = path

    def is_valid(self):
        # Check for valid number of missionaries and cannibals on both sides
        m_right = 3 - self.m
        c_right = 3 - self.c

        if self.m < 0 or self.c < 0 or m_right < 0 or c_right < 0:
            return False
        if self.m > 0 and self.m < self.c:
            return False
        if m_right > 0 and m_right < c_right:
            return False
        return True

    def is_goal(self):
        return self.m == 0 and self.c == 0 and self.b == 0

    def get_successors(self):
        moves = [
            (1, 0), (2, 0),  # 1 or 2 missionaries
            (0, 1), (0, 2),  # 1 or 2 cannibals
            (1, 1)           # 1 missionary and 1 cannibal
        ]
        successors = []

        for m_move, c_move in moves:
            if self.b == 1:
                new_state = State(self.m - m_move, self.c - c_move, 0, self.path + [self])
            else:
                new_state = State(self.m + m_move, self.c + c_move, 1, self.path + [self])

            if new_state.is_valid():
                successors.append(new_state)

        return successors

    def __repr__(self):
        return f"(Left-> M: {self.m}, C: {self.c}, Boat: {'Left' if self.b else 'Right'})"

def solve():
    start = State(3, 3, 1)
    queue = deque([start])
    visited = set()

    while queue:
        state = queue.popleft()

        if (state.m, state.c, state.b) in visited:
            continue
        visited.add((state.m, state.c, state.b))

        if state.is_goal():
            path = state.path + [state]
            print("Missionaries and Cannibals solution:")
            for step in path:
                print(step)
            return

        for successor in state.get_successors():
            queue.append(successor)

    print("No solution found.")

# Run it
solve()
