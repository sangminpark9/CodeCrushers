import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
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
            new_dis = dis + weight
            if new_dis < distances[neighbor]:
                distances[neighbor] = new_dis
                paths[neighbor] = paths[node] + [(node, neighbor)]
                heapq.heappush(queue, (new_dis, neighbor))
    return paths

for i in range(1, V+1):
    i_paths = dijkstra(i)
    for j in range(1, V+1):
        if i == j:
            print('-', end=' ')
        else:
            print(i_paths[j][0][1],end=' ')
    print() # 한 칸 띄우기


