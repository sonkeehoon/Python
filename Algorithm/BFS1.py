from collections import deque

graph = [
    [],
    [3, 2],
    [6, 7],
    [4, 5],
    [3],
    [3],
    [2],
    [2]
    ]


def bfs(graph, n, root):
    visited = [False]*n
    
    q = deque()
    q.append(root)
    
    while q:
        node = q.popleft()
        print(node)
        
        for cur in graph[node]:
            if visited[cur]:
                continue
            visited[cur] = True
            q.append(cur)

n = len(graph)
root = 1
bfs(graph, n, root)
                
            
    
    
    