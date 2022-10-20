import sys
input=sys.stdin.readline
N=int(input())
lst=list(map(int,input().split()))
M=int(input())
cards=list(map(int,input().split()))
res=[0]*M
lst=set(lst)
for i in range(M):
    if cards[i] in lst:
        res[i]=1
for i in res:
    print(i,end=' ')