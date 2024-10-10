import sys
import heapq

V, E, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    v,e,w = map(int, sys.stdin.readline().split())
    graph[v].append((e,w))

def dijkstra(start, end): # 그냥 X부터 시작해서, distance가 가장 먼 곳을 출력한다면?

    distances = [float('INF')] * (V+1)
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neigbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neigbor]:
                distances[neigbor] = distance
                heapq.heappush(queue, (distance, neigbor))
    if start == X: # 다시 돌아간다면 distance를 반환하면서 종료
        return distances
    else:
        back_distance = dijkstra(end, start)
    
    return distances[X] + back_distance[start]

big = 0
for i in range(1,V+1): # 1부터 V까지
    tmp = dijkstra(i, X)
    if i != X and tmp > big :
        big = tmp

print(big)
