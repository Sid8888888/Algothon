import heapq

def bidirectional_dijkstra(n, graph, delivery_points, start=1):
    
    def dijkstra(start, graph, n):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]  
        while pq:
            current_dist, node = heapq.heappop(pq)
            if current_dist > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                new_dist = current_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        return dist

    
    reverse_graph = {i: [] for i in range(1, n + 1)}
    for u in graph:
        for v, w in graph[u]:
            reverse_graph[v].append((u, w))

    
    dist_from_start = [float('inf')] * (n + 1)
    dist_from_end = {dp: [float('inf')] * (n + 1) for dp in delivery_points}

    dist_from_start[start] = 0
    pq_start = [(0, start)]  

    
    while pq_start:
        current_dist, node = heapq.heappop(pq_start)
        if current_dist > dist_from_start[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist_from_start[neighbor]:
                dist_from_start[neighbor] = new_dist
                heapq.heappush(pq_start, (new_dist, neighbor))

    
    min_dist = float('inf')
    pq_end = []
    for dp in delivery_points:
        dist_from_end[dp][dp] = 0
        heapq.heappush(pq_end, (0, dp))  

    while pq_end:
        current_dist, node = heapq.heappop(pq_end)
        for neighbor, weight in reverse_graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist_from_end[node][neighbor]:
                dist_from_end[node][neighbor] = new_dist
                heapq.heappush(pq_end, (new_dist, neighbor))

    
    for dp in delivery_points:
        if dist_from_start[dp] + dist_from_end[dp] < min_dist:
            min_dist = dist_from_start[dp] + dist_from_end[dp]

    return min_dist



n = 5  
m = 6  
roads = [
    (1, 2, 10),  
    (1, 3, 5),
    (2, 3, 2),
    (3, 4, 3),
    (2, 4, 1),
    (4, 5, 7)
]


graph = {i: [] for i in range(1, n + 1)}
for u, v, w in roads:
    graph[u].append((v, w))

delivery_points = [2, 3, 5]  


result = bidirectional_dijkstra(n, graph, delivery_points)
print(f"Shortest delivery time: {result}")
