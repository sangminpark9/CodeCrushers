def solution(n, computers):
    def DFS(v):
        visited[v] = True
        for i in range(n):
            if computers[v][i] == 1 and not visited[i]:
                DFS(i)

    visited = [False] * n
    cnt = 0

    for i in range(n):
        if not visited[i]:
            DFS(i)
            cnt += 1
    
    return cnt

