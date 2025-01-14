import time

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

def dfs(graph, root):
    visited = [False]*n
    time.sleep(1)
    
    stack = []
    stack.append(root)
    
    while stack:
        time.sleep(1)
        node = stack.pop()
        print(node,stack)
        for cur in graph[node]:
            stack.append(cur)


n = len(graph)
root = 1
dfs(graph, root)