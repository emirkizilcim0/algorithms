import heapq 



def dijkstra(graph, start_node):
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start_node] = 0
    min_heap = [(0, start_node)]  # (distance, node)

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > shortest_distances[current_node]:
            continue
        
        # print(graph[current_node].items())
        for neighbor, weight in graph[current_node].items():
            distance = weight + current_distance

            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return shortest_distances
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph=graph, start_node='A'))
