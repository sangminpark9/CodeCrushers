from collections import deque
    
def solution(rectangle, characterX, characterY, itemX, itemY):
    field = [[-1] * 102 for _ in range(102)]

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, r)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x < x2 and y1 < y < y2:
                    field[x][y] = 0
                elif field[x][y] != 0:
                    field[x][y] = 1
    
    q = deque()
    q.append((characterX * 2,characterY * 2, 0))
    visited = [[False] * 102 for _ in range(102)]
    visited[characterX *2][characterY*2]
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    while q:
        x, y, step = q.popleft()
        if (x,y) == (itemX *2, itemY *2 ):
            return step // 2
    
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 102 and 0 <= ny < 102 and visited[nx][ny] == False and field[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx,ny,step + 1))

    return 0
