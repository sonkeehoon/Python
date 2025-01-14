import time

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

def dfs(graph, root):
    # visited = [False]*(n+1)
    time.sleep(1)
    
    stack = []
    stack.append(root)
    print(root)
    
    while stack:
        node = stack.pop()
        
        for cur in graph[node]:
            if not graph[cur]:
                continue
            print(cur)
            stack.append(cur)


n = len(graph)
root = 1
dfs(graph, root)