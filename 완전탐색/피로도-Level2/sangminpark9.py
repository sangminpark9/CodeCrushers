answer = 0

def dfs(k, dungeons, visited, count):
    global answer
    answer = max(answer, count)
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            new_visited = visited.copy() 
            new_visited[i] = True 
            dfs(k - dungeons[i][1], dungeons, new_visited, count + 1)  

def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, dungeons, visited, 0)
    return answer
