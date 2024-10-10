import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    v,e,w = map(int, sys.stdin.readline().split())
    graph[v].append((e,w))
    graph[e].append((v,w)) # 무방향

def dijkstra(start):
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

n1, n2 = map(int, sys.stdin.readline().split())
small = float('INF')
one_to_nx_distances = dijkstra(1)
###
n1_to_n2_distances = dijkstra(n1)
n2_to_V_distances = dijkstra(n2)
one_n1_n2_V = one_to_nx_distances[n1] + \
              n1_to_n2_distances[n2] + \
              n2_to_V_distances[V]
###
n2_to_n1_distances = dijkstra(n2)
n1_to_V_distances = dijkstra(n1)
one_n2_n1_V = one_to_nx_distances[n2] + \
              n2_to_n1_distances[n1] + \
              n1_to_V_distances[V]

small = one_n1_n2_V if one_n1_n2_V < one_n2_n1_V else one_n2_n1_V

if small == float('INF'):
    print(-1)
else:
    print(small)
