import sys
input=sys.stdin.readline
N=int(input())
lst=list(map(int,input().split()))
set_lst=sorted(list(set(lst)))
d={}
for i in range(len(set_lst)):
    d[set_lst[i]]=i
for i in lst:
    print(d[i],end=' ')


