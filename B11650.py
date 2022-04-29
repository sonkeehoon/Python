import sys
input=sys.stdin.readline
N=int(input())
lst=[]
for i in range(N):
    x,y=map(int,input().split())
    lst.append([x,y])
lst.sort()
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j],end=' ')
    print()


