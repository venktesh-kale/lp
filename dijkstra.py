def dijkstra(graph, start, end, visited=None, distances=None, predecessors=None):
    if visited is None:
        visited = set()
    if distances is None:
        distances = {vertex: float('inf') for vertex in graph}
    if predecessors is None:
        predecessors = {}
    distances[start] = 0

    minDistv = None
    for vertex in graph:
        if vertex not in visited:
            if minDistv is None or distances[vertex] < distances[minDistv]:
                minDistv = vertex

    if minDistv is None:
        return distances[end], _shortest_path(predecessors, start, end)

    visited.add(minDistv)

    for neighbor, weight in graph[minDistv].items():
        new_distance = distances[minDistv] + weight
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            predecessors[neighbor] = minDistv

    return dijkstra(graph, start, end, visited, distances, predecessors)

def _shortest_path(predecessors, start, end):
    path = []
    current = end
    while current != start:
        path.insert(0, current)
        current = predecessors[current]
    path.insert(0, start)
    return path


# Example usage:
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 3, 'D': 4},
    'C': {'A': 1, 'B': 3, 'D': 2},
    'D': {'B': 4, 'C': 2}
}

start = 'A'
end   = 'D'
shortest_distance, shortest_path = dijkstra(graph, start, end)
print(f"The shortest distance from {start} to {end} is {shortest_distance}")
print(f"The shortest path is {' -> '.join(shortest_path)}")