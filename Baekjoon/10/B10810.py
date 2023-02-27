import sys
input = sys.stdin.readline
N,M = map(int,input().split())
lst = [0]*N
for _ in range(M):
    i,j,k = map(int,input().split())
    lst[i-1:j] = [k]*(j-(i-1))
print(*lst)
    