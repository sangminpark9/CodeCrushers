from collections import deque
    
def solution(rectangle, characterX, characterY, itemX, itemY):
    filed = [[-1] * 102 for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = r[0] *2, r[1] *2, r[2] *2, r[3] *2
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if x1 < x < x2 and y1 < y < y2:
                    filed[x][y] = 0
                elif filed[x][y] != 0:                   # 테두리는 1
                    filed[x][y] = 1
    
    q = deque()
    q.append((characterX *2, characterY *2, 0))
    
    visited = [[False] * 102 for _ in range(102)]
    visited[characterX *2][characterY*2] = True

    dx, dy = [1,-1,0,0], [0,0,1,-1]
    while q:
        cx, cy, steps = q.popleft()
        if (cx, cy) == (itemX *2 , itemY * 2):
            return steps // 2
    
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < 102 and 0 <= ny < 102:
                if visited[nx][ny] == False and filed[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, steps + 1))
                    
    return 0
