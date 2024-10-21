from collections import deque
import sys

def make_flag(dx, dy, c):
    if dx == [0,0,1,0]: # 오른쪽으로 이동 중이었다면
        if c == 'L':
            dy = [0,-1,0,0]
        elif c == 'D':
            dy = [1,0,0,0]
        dx = [0, 0, 0, 0]
    
    elif dx == [0,0,0,-1]: # 왼쪽으로 이동 중이었다면
        if c == 'L':
            dy = [1,0,0,0]
        elif c == 'D':
            dy = [0,-1,0,0]
        dx = [0,0,0,0]
        
    elif dy == [1,0,0,0]: # 아래로 이동 중이었다면
        if c == 'L':
            dx = [0,0,1,0]
        elif c == 'D':
            dx = [0,0,0,-1]
        dy = [0,0,0,0]
        
    elif dy == [0,-1,0,0]: # 위로 이동 중이었다면
        if c == 'L':
            dx = [0,0,0,-1]
        elif c == 'D':
            dx = [0,0,1,0]
        dy = [0,0,0,0]

    return dx, dy

N = int(input())
K = int(input())

apple = []
snake = []
for _ in range(K):
    row, col = map(int, sys.stdin.readline().rstrip().split())
    apple.append((col -1 , row - 1))

L = int(input())
for _ in range(L):
    x, c = sys.stdin.readline().rstrip().split()
    x = int(x)
    snake.append((x,c))

dx,dy = [0,0,1,0], [0,0,0,0]
x, y = 0, 0
# -1,1,-1,1 이렇게 갈건데
# 위 아래 오른쪽 왼쪽 순서임
times = 0
q = deque()
length = 1
j = 0
while True:
    for i in range(4):# dx, dy에 따라서 이동
        x, y = x + dx[i], y + dy[i]
    if 0 <= x < N and 0 <= y < N: # 범위 안에 있다면~ 
        if (x,y) in q: # 자신의 몸과 부딫친다면
            print(times + 1)
            exit()
        elif (x,y) in apple: # 사과를 먹으면 사과도 지워야하는구나
            apple.remove((x,y))
            q.append((x,y))
            length += 1
            
        elif (x,y) not in apple:
            q.append((x,y))
            if length < len(q):
                q.popleft() # 꼬리 삭제
        times += 1
    else: # 지정된 범위를 벗어난다면
        print(times + 1)
        exit()
    if j < len(snake):
        if times == snake[j][0]:
            dx, dy = make_flag(dx, dy, snake[j][1])
            j += 1
    
    
    

