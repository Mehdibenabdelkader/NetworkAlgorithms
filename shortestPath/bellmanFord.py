def bellman_ford(vertices, edges, start):
    distances = {i: float('infinity') for i in range(vertices)}
    distances[start] = 0

    for _ in range(vertices - 1):
        for u, v, weight in edges:
            if distances[u] != float('infinity') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    for u, v, weight in edges:
        if distances[u] != float('infinity') and distances[u] + weight < distances[v]:
            print("Graph contains a negative weight cycle")
            return None

    return distances

if __name__ == "__main__":
    vertices = 5
    edges = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)
    ]
    start_node = 0
    distances = bellman_ford(vertices, edges, start_node)

    if distances:
        print("Shortest distances from start node:", distances)