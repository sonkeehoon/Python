# 90%에서 시간 초과가 뜬다
# 남의 코드를 그대로 제출하긴 싫어서 이대로 두려고 한다
import sys
from collections import defaultdict,deque
input = sys.stdin.readline

N,M,R = map(int,input().split())
# 정점의 수 N, 간선의 수 M, 시작 정점 R

graph = defaultdict(list)
for _ in range(1,M+1):
    u,v = map(int,input().split())
    # u와 v 연결
    graph[u].append(v)
    graph[v].append(u)
# 각 key의 value 들을 오름차순 정렬
for k in graph:
    graph[k].sort()
visited = [0]*(N+1)
visited[R] = 1
queue = deque([R])
cnt = 2
# graph = {1: [2,4], 2: [1,3,4], 3: [2,4], 4: [1,2,3]}
while queue:
    tmp = queue.pop()
    
    for g in graph[tmp]:
        
        if visited[g] > 0: # 다음 노드가 방문 한거면 pass
            continue
        
        queue.append(tmp) 
        visited[g] = cnt
        cnt += 1
        queue.append(g)
        break
    
print(*visited[1:], sep='\n')