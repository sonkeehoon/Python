# 알고리즘 수업 - 너비 우선 탐색 1 : https://www.acmicpc.net/problem/24444
from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int,input().split()) # 정점의 수 N, 간선의 수 M, 시작 정점 R

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for nodes in graph:
    nodes.sort()
    
queue = deque([R])
visited = [False] * (N + 1)
visited[R] = True

res = [0] * (N + 1)
order = 1
res[R] = order

while queue:
    cur = queue.popleft()
    
    for node in graph[cur]:
        if not visited[node]:
            visited[node] = True
            queue.append(node)
            order += 1
            res[node] = order

print(*res[1:], sep = '\n')
