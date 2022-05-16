import sys
input=sys.stdin.readline
N=int(input())
lst=[]
for i in range(N):
    x,y=map(int,input().split())
    lst.append([y,x])
lst.sort()
for i in range(len(lst)):
    for j in range(len(lst[0])):
        print(lst[i][1-j],end=' ')
    print()