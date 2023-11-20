# 최대 힙 : https://www.acmicpc.net/problem/11279

import heapq
import sys
input = sys.stdin.readline

N = int(input()) # 연산의 개수
heap = [] # 최대 힙
for _ in range(N): 
    x = int(input()) # 연산에 대한 정보를 나타내는 x
    if x == 0:
        
        if heap:
            print(-heapq.heappop(heap)) # heap에서 pop 연산
            continue
        
        print(0)
        continue
    
    heapq.heappush(heap, -x) # heap안에 -x를 삽입
    
    
