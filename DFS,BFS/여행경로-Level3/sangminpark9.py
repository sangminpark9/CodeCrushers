from collections import deque

def solution(tickets):
    graph = {}
    for start, end in tickets:
        if start not in graph.keys():
            graph[start] = [end]
        else:
            graph[start].append(end)
    
    def dfs(airport,path):
        if len(path) == len(tickets) + 1:
            return path
        if airport not in graph:
            return None
        
        for _ in range(len(graph[airport])):
            next_airport = graph[airport].pop(0)
            result = dfs(next_airport, path + [next_airport])
            graph[airport].append(next_airport)
        
            if result:
                return result
            
        return None
            
    return dfs('ICN', ['ICN'])
