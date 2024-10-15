import sys
import heapq

n = int(input())
queue = []

for _ in range(n):
    tmp = int(sys.stdin.readline().rstrip())
    heapq.heappush(queue,tmp)
    
output = 0
while len(queue) > 1:
    a = heapq.heappop(queue)
    b = heapq.heappop(queue)
    output += a + b
    heapq.heappush(queue, a + b)

print(output)

# 5
# 73
# 18
# 14
# 24
# 13
# 13 + 14 + 18+ 24 + 27 + 44 + 71 + 73
#  27         44        71
# 169 + 44 + 73
# 209 + 4 + 73
# 213 + 73
