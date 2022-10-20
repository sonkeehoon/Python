import sys
input=sys.stdin.readline
N,M=map(int,input().split())
lst=[]
d={}
for i in range(N):
    x=input().rstrip()
    lst.append(x)
    d[x]=i+1
for i in range(M):
    y=input().rstrip()
    if y in d:
        print(d[y])
        continue
    print(lst[int(y)-1])