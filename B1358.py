import sys
input=sys.stdin.readline
W,H,X,Y,P=map(int,input().split())
lst=[]
for i in range(P):
    x,y=map(int,input().split())
    lst.append([x,y])
    