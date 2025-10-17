# 최단경로: https://www.acmicpc.net/problem/1753
import sys, heapq
input = sys.stdin.readline
INF = float('inf')

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

min_dist = [INF] * (V + 1)
min_dist[K] = 0

pq = [(0, K)]  # (거리, 노드)

while pq:
    dist, u = heapq.heappop(pq)
    if dist > min_dist[u]:
        continue
    for v, w in graph[u]:
        new_dist = dist + w
        if new_dist < min_dist[v]:
            min_dist[v] = new_dist
            heapq.heappush(pq, (new_dist, v))

for d in min_dist[1:]:
    print("INF" if d == INF else d)
