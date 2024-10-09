import heapq

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    v,e,w = map(int, input().split())
    graph[v].append((e,w))

## 입력 끝

def dijkstra(start, V, E):
    distances = [float('INF')] * (V+1)
    distances[start] = 0
    queue = [(0,start)]
    
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances
    
distances = dijkstra(K,V,E)

for i in range(1,len(distances)):
    if distances[i] == float('INF'):
        print('INF')
    else:
        print(distances[i])
