def dfs(graph, start, visited):
    # 현재 노드를 방문 처리
    visited[start] = True
    # 노드 탐색!!
    print(start, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for neighbor in graph[start]:
      if not visited[neighbor]:
        dfs(graph, neighbor, visited)

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

visited = [False] * len(graph_heap)

# DFS 함수 호출
dfs(graph_heap, 1, visited)
print()

# graph_circular
# 방문 정보
visited = [False] * len(graph_circular)

# DFS 함수 호출
dfs(graph_circular, 1, visited)
print()

# graph_delivery
# 방문 정보
visited = [False] * len(graph_delivery)

# DFS 함수 호출
dfs(graph_delivery, 1, visited)
print()