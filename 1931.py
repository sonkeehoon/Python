import sys
input=sys.stdin.readline
N=int(input())
t=[]
k,cnt=0,0
for i in range(N):
    x,y=map(int,input().split())
    t.append([x,y])
t.sort(key=lambda x: x[0])
t.sort(key=lambda x: x[1])
for i in range(N):
    if t[i][0]>=k:
        cnt+=1
        k=t[i][1]
print(cnt)