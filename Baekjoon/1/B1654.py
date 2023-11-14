# 랜선 자르기 : https://www.acmicpc.net/problem/1654
import sys
input = sys.stdin.readline

K, N = map(int,input().split()) # 랜선의 개수, 필요한 랜선의 개수
# 항상 K <= N 이어야 한다
lines = []
for _ in range(K): # K개 랜선의 길이
    lines.append(int(input()))
start, end = 1, max(lines) + 1
while start < end:
    total = 0
    mid = (start + end) // 2
    for line in lines:
        total += line//mid
    if total < N:
        if end == mid:
            break
        end = mid
    else:
        if start == mid:
            break
        start = mid
print(mid)
        
    
    