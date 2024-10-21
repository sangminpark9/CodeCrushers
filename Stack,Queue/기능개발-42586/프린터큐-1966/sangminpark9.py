import sys
from collections import deque


t = int(input())

for _ in range(t):
    n, d = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int,input().split()))
    # 입력 끝
    q = deque()
    q += list(enumerate(arr, 0))
    
    output = 0
    while q:
        number, weight = q.popleft()
        big_weight = max(arr)
        
        if weight != big_weight:
            q.append((number, weight))
            
        else: # 현재 중요도가 최대라면 ㄹ력
            if number == d:
                print(output + 1)
                break
            arr.remove(big_weight)
            output += 1
        
