import sys
from collections import defaultdict,deque
import heapq
input = sys.stdin.readline

N, M, R = map(int,input().split())
# 정점의 수 N, 간선의 수 M, 시작 정점 R

graph = defaultdict(list)
for _ in range(1,M+1):
    u,v = map(int,input().split())
    # u와 v 연결
    graph[u].append(v)
    graph[v].append(u)

for k in graph:
    heapq.heapify(graph[k])
visited = [0]*(N+1)
visited[R] = 1
# print(graph)
queue = deque([R])
cnt = 1
# graph = {1: [2,4], 2: [1,3,4], 3: [2,4], 4: [1,2,3]}
while queue:
    tmp = queue.pop()
    heap = graph[tmp]
    if not heap:
        continue
    while heap:
        next = heapq.heappop(heap)
        if visited[next] == 0:
            cnt += 1
            visited[next] = cnt
            break
    # print(tmp, next, queue, cnt)
    queue.append(tmp)
    queue.append(next)
    
    
        
        
    # for g in graph[tmp]:
        
    #     if visited[g] > 0: # 다음 노드가 방문 한거면 pass
    #         continue
        
    #     queue.append(tmp) 
    #     visited[g] = cnt
    #     cnt += 1
    #     queue.append(g)
    #     break
    
for v in visited[1:]:
    print(v)