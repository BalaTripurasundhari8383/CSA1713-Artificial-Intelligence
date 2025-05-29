import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current Node
        self.h = 0  # Heuristic cost from current Node to end
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    # Manhattan Distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, end):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    end_node = Node(end)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            path.reverse()
            cost = len(path) - 1
            return path, cost

        x, y = current_node.position
        neighbors = [(x+dx, y+dy) for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]]

        for next_pos in neighbors:
            nx, ny = next_pos
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == 1 or next_pos in closed_set:
                    continue

                neighbor_node = Node(next_pos, current_node)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = heuristic(next_pos, end_node.position)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                if any(open_node.position == neighbor_node.position and open_node.f <= neighbor_node.f for open_node in open_list):
                    continue

                heapq.heappush(open_list, neighbor_node)

    return None, 0  # No path found

# Example usage:
if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    path, cost = a_star(grid, start, end)
    
    if path:
        print("Path:", path)
        print("Cost:", cost)
    else:
        print("No path found.")
