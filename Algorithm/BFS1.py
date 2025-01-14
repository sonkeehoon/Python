from collections import deque

graph = [
    [],
    [3, 2],
    [6, 7],
    [4, 5],
    [3],
    [3],
    [2],
    [7]
    ]


def bfs(graph, n, root):
    visited = [False]*n
    
    
    q = deque()
    q.append(root)
    print(root)
    
    while q:
        node = q.popleft()
        
        for cur in graph[node]:
            if visited[cur]:
                continue
            visited[cur] = True
            print(cur)
            q.append(cur)

n = len(graph)
root = 1
bfs(graph, n, root)
                
            
    
    
    