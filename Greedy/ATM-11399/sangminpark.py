import sys

n = int(input())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr2 = [(x,idx) for x,idx in enumerate(arr,0)]
arr2 = sorted(arr2, key = lambda x:x[1] )
# 1 +// 1 + 2 //+ 1 + 2+ 3+// 1+ 2+ 3+ 3+// 1+ 2 + 3 + 3 + 4
output = 0
for _, ele in arr2:
    output += n*ele
    n -= 1
print(output)
