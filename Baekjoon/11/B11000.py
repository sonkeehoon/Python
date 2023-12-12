# 강의실 배정 : https://www.acmicpc.net/problem/11000
import sys
import heapq
input = sys.stdin.readline
N = int(input())

tmp = sorted([tuple(map(int, input().split())) for _ in range(N)],
             key = lambda x : x[0])
# for _ in range(N):
#     tmp.append(list(map(int, input().split())))

# # tmp.sort(key = lambda x : x[0])
# tmp = sorted(tmp, key = lambda x : x[0])
heap = []
heapq.heappush(heap, tmp[0][1])
for i in range(1, N):
    heapq.heappush(heap, tmp[i][1])
    if tmp[i][0] >= heap[0]:
        heapq.heappop(heap)
    #     heapq.heappush(heap, t)
    # else:
    #     heapq.heappush(heap, t)
print(heap)
print(len(heap))
        
    
    
    
    


    
    