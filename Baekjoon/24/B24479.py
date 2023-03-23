import sys
from collections import defaultdict,deque
input = sys.stdin.readline
import time

N,M,R = map(int,input().split())
# 정점의 수 N, 간선의 수 M, 시작 정점 R
graph = defaultdict(list)
# print(graph)
for _ in range(1,M+1):
    u,v = map(int,input().split())
    # u와 v는 연결
    graph[u].append(v)
# 각 key의 value 들을 오름차순 정렬
for k in graph.keys():
    graph[k].sort()
    graph[k] = deque(graph[k])
order = defaultdict(int)
order[R] = 1
queue = deque([R])
cnt = 2
print(graph)
# graph = {1: [2, 4], 2: [3, 4], 3: [4]}
while queue:
    tmp = queue[-1] # 시작 노드 지정
    print(queue,graph, tmp, order)
    if not graph[tmp]:
        queue.pop()
        continue
    
    for i in graph[tmp]:
        if i in order.keys(): # 이미 방문 했다면
            continue
        order[i] = cnt
        cnt += 1
        queue.append(i)
        
        break
    time.sleep(2)
print(order,cnt)
for i in range(1,N+1):
    print(order[i])
        
        
        
    
        
    
    
    
    

        
    
    

