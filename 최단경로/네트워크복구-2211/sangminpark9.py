import sys
import heapq

V,E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    v,e,w = map(int, sys.stdin.readline().split())
    graph[v].append((e,w))
    graph[e].append((v,w))

def dijkstra(start):
    distances = [float('INF')] * (V+1)
    distances[start] = 0
    paths = [[] for _ in range(V+1)]
    queue = [(0,start)]
    
    while queue:
        dis, node = heapq.heappop(queue)
        if dis > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dis  = dis + weight
            if new_dis < distances[neighbor]:
                distances[neighbor] = new_dis
                paths[neighbor] = paths[node] + [(node, neighbor)]
                heapq.heappush(queue, (new_dis, neighbor))
    
    return distances, paths

_, paths = dijkstra(1)
output, cnt = set(), 0
for i in range(1, len(paths)):
    if len(paths[i]) >= 1:
        for path in paths[i]:
            if path not in output:
                cnt += 1
                output.add(path)
              
print(len(output))
for a,b in output:
    print(a,b)
