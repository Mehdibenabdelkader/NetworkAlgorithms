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