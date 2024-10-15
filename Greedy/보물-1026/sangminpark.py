import sys

n = int(input())

A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

sorted_indices = sorted(range(n), key=lambda x: B[x],reverse=True)
tmp = sorted(A)

for item,idx in zip(tmp, sorted_indices):
    A[idx] = item

output = 0
for i in range(n):
    output += A[i] * B[i]
print(output)
