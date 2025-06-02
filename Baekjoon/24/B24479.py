# 알고리즘 수업 - 깊이 우선 탐색 1 : https://www.acmicpc.net/problem/24479
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int,input().split()) # 정점의 수 N, 간선의 수 M, 시작 정점 R

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for e in graph:
    e.sort()

visited = [False] * (N + 1)
visited[R] = True
res = [0] * (N + 1)
order = 1
res[R] = order

def dfs(cur):
    global order
    
    for dest in graph[cur]:
        if not visited[dest]:
            order += 1
            res[dest] = order
            visited[dest] = True
            dfs(dest)
            
dfs(R)

print(*res[1:], sep = '\n')