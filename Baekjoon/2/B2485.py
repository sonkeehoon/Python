import sys,math
input = sys.stdin.readline
N = int(input())
trees = [int(input()) for _ in range(N)]

dist = [trees[i+1] - trees[i] for i in range(len(trees)-1)]
size = len(dist)
idx = 2
gcd = math.gcd(dist[0],dist[1]) # gcd(4,6) = 2
while idx < size :
    gcd = math.gcd(gcd, dist[idx])
    idx += 1
    
start,end = trees[0],trees[-1]
cnt = 0
for j in dist: # 시간을 줄이기 위한 전략
    if j == gcd:
        continue
    cnt += (j//gcd)-1
print(cnt)
