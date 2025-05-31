# N번째 큰 수 : https://www.acmicpc.net/problem/2075

import heapq
import sys
input = sys.stdin.readline
N = int(input())

heap = list(map(int, input().split()))
heapq.heapify(heap)
    
for _ in range(N-1):
    
    for e in map(int, input().split()):
        heapq.heappush(heap, e)
        
    for __ in range(N):
        heapq.heappop(heap)
        

print(heap[0])
        

# for _ in range(N-1):
#     heapq.heappop(heap)
    
# print(-heapq.heappop(heap))
