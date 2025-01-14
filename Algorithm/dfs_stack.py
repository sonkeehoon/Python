def dfs_stack(graph, start):
    # 현재 노드를 방문 처리
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # 노드 탐색!
            print(node, end= ' ')
            for neighbor in reversed(graph[node]): # 왼쪽 노드부터 넣기 위해!
                if neighbor not in visited:
                    stack.append(neighbor)
# 인접 리스트로 표현된 그래프
graph_heap = [
    [],
    [2, 3],
    [1, 4, 5],
    [1, 6],
    [2],
    [2],
    [3]
]

graph_circular = [
    [],
    [2, 3],
    [1, 4],
    [1, 4],
    [2, 3],
]

graph_delivery = [
    [],
    [2, 4],
    [1, 3, 5],
    [2, 5],
    [1, 5],
    [2, 3, 4]
]
dfs_stack(graph_heap, 1)
print()
dfs_stack(graph_circular, 1)
print()
dfs_stack(graph_delivery, 1)
print()