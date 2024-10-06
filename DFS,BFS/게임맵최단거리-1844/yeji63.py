from collections import deque
def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[False]*m for _ in range(n)]
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        
        while queue:
            x, y = queue.popleft()
            visited[x][y] = True
    
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1 and visited[nx][ny] == False:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
        print(maps)
            
        return maps[n-1][m-1]
            
    
    answer = bfs(0, 0)
    if answer == 0 or answer == 1:
        answer = -1
    
    return answer
