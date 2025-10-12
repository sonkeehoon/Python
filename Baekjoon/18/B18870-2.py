# 좌표 압축: https://www.acmicpc.net/problem/18870
# heapq 풀이(속도 느림, 메모리 적게 씀)
import sys
import heapq
input = sys.stdin.readline
n = int(input())
X = list(map(int, input().split()))
d = {}

heap = list(set(X))
heapq.heapify(heap)

idx = 0
while heap:
    tmp = heapq.heappop(heap)
    d[tmp] = idx
    idx += 1

for i in range(len(X)):
    X[i] = d[X[i]]

print(*X)
