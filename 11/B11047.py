import sys
input=sys.stdin.readline
N,K=map(int,input().split())
lst=[0]
cnt=0
for _ in range(N):
    lst.append(int(input()))
for i in range(N,0,-1):
    if lst[i]<=K:
        cnt+=K//lst[i]
        K%=lst[i]
    elif K==0:
        break
print(cnt)