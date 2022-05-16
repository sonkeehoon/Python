import sys
input=sys.stdin.readline
K=int(input())
d={}
lst=[]
for i in range(6):
    x,y=map(int,input().split())
    lst.append(y)
    d[y]=x
res=lst+lst
for i in range(6):
    if d[res[i]]==d[res[i+2]]:
        print((res[i+4]*res[i+5]-(res[i+1]*res[i+2]))*K)
        break