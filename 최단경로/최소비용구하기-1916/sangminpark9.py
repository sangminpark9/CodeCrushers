import sys
import heapq

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
for i in range(E):
    v,e,w = map(int,sys.stdin.readline().split())
    graph[v].append((e,w))
start, end = map(int,sys.stdin.readline().split())

def dijkstra(start):
    distances = [float('INF')] * (V+1)
    distances[start] = 0
    queue = [(0,start)] # distance, vertex
    
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neigbor, weight in graph[current_vertex]: # 이웃 조회
            distance = current_distance + weight
            if distance < distances[neigbor]:
                distances[neigbor] = distance
                heapq.heappush(queue, (distance, neigbor))
    return distances

start_distances = dijkstra(start)
print(start_distances[end])
