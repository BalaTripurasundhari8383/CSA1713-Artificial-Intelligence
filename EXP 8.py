def dfs_recursive(graph, node, visited=None, traversal_order=None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []

    visited.add(node)
    traversal_order.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal_order)
    
    return traversal_order

# Sample input graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call DFS starting from node 'A'
result = dfs_recursive(graph, 'A')
print("DFS Recursive Traversal Order:", result)
