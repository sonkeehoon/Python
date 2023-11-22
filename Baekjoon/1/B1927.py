# 최소 힙 : https://www.acmicpc.net/problem/1927

import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    
    if x == 0:
        
        if heap:
            print(heapq.heappop(heap))
            
        else:
            print(0)
            
    else:
        heapq.heappush(heap, x)