import sys
from collections import deque

A, B = map(int, sys.stdin.readline().rstrip().split())

def bfs(start, end):
    q = deque()
    q.append((start, 1)) # start, step = 1
    
    while q:
        n, step = q.popleft()
        if n == B:
            return step
        if n > end:
            continue
    
        n1 = 2 * n
        if n1 <= end:
            q.append((n1, step + 1))
            
        n2 = int(str(n) + '1')
        if n2 <= end:
            q.append((n2, step + 1))
        
    return -1

output = bfs(A, B)
print(output)
