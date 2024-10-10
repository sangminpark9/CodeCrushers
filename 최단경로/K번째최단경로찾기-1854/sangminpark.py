import sys
import heapq

V,E,K = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    v,e,w = map(int,sys.stdin.readline().split())
    graph[v].append((e,w))
    
def dikjstra(start):
    distances = [[] for _ in range(V+1)]
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if len(distances[current_vertex]) == K:
            continue
        distances[current_vertex].append(current_distance)
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            heapq.heappush(queue, (distance, neighbor))
    
    return distances

distences = dikjstra(1)

for i in range(1,len(distences)):
    if len(distences[i]) < K:
        print(-1)
    else:
        print(distences[i][K-1])
