# 카드 정렬하기: https://www.acmicpc.net/problem/1715
import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = [int(input()) for _ in range(N)]
total = 0
heapq.heapify(heap)

while len(heap) >= 2:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    p_sum = first + second
    total += p_sum
    heapq.heappush(heap, p_sum)
    
print(total)


    
    

