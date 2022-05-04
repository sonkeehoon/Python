import sys
N=int(sys.stdin.readline())
cnt=[0]*10001
for _ in range(N):
    x=int(sys.stdin.readline())
    cnt[x]+=1
for i in range(1,10001):
    for j in range(cnt[i]):
        print(i)