import sys
from collections import deque

n = int(input())

graph = {}
for _ in range(n-1):
    v, e = map(int, sys.stdin.readline().rstrip().split())
    if v not in graph.keys():
        graph[v] = [e]
    else:
        graph[v].append(e)
    if e not in graph.keys():
        graph[e] = [v]
    else:
        graph[e].append(v)
        
output = {x:-1 for x in graph.keys()}
# 입력 끝
def bfs():
    q = deque()
    q.append((1,1)) # current ndoe, parent node
    while q:
        node, parent = q.popleft()
        output[node] = parent
        for neighbor in graph[node]: # node의 neighbor검색
            if neighbor != 1 and output[neighbor] == -1:
                q.append((neighbor,node))
            
    return # 응답이 없는 경우

bfs()
keys = sorted(output.keys())
for key in keys:
    if key == 1:
        continue
    print(output[key])
