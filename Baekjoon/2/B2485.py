import sys
from math import gcd
input = sys.stdin.readline
N = int(input())

dist = []
tmp,tmp2 = 0,0
# trees 리스트는 필요 없음
# dist = [trees[i+1] - trees[i] for i in range(len(trees)-1)]
for i in range(N): # 시간을 줄이기 위해 나무 사이의 거리만 dist에 append
    if i == 0:
        tmp = int(input())
    else:
        tmp2 = int(input())
        dist.append(tmp2-tmp)
        tmp = tmp2
        
size = len(dist)
idx = 2
gcdnum = gcd(dist[0],dist[1]) # gcd(4,6) = 2
while idx < size :
    gcdnum = gcd(gcdnum, dist[idx])
    idx += 1
cnt = 0
for j in dist: # 시간을 줄이기 위한 전략
    cnt += (j//gcdnum)-1
print(cnt)
