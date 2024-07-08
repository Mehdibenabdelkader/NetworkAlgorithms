import heapq

def dijkstra(graph, start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (cost, node)

    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def shortest_path(previous_nodes, start, target):
    path = []
    node = target

    while node is not None:
        path.append(node)
        node = previous_nodes[node]

    path.reverse()

    return path

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 1},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 1, 'C': 1}
    }
    start_node = 'A'
    end_node = 'D'

    distances, previous_nodes = dijkstra(graph, start_node)
    print("Shortest distances from start node:", distances)
    print("Shortest path from start to end node:", shortest_path(previous_nodes, start_node, end_node))