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

def dfs(graph, n, root):
    visited = [False]*n
    
    stack = []
    stack.append((root,0))
    
    while stack:
        node, length = stack.pop()
        visited[node] = True
        print(node, stack)
        
        length += 1
        for cur in graph[node]:
            if cur == target:
                print((target, length))
                return 
            if not visited[cur]:
                stack.append((cur,length))


n = len(graph)
root = 1
target = 5
dfs(graph, n, root)