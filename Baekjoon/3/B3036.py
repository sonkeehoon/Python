import sys
from math import gcd
input=sys.stdin.readline
N=int(input())
lst=list(map(int,input().split()))
res=[]
for i in range(1,N):
    cpy_lst=lst[:]
    while gcd(cpy_lst[0],cpy_lst[i])!=1:
        n=gcd(cpy_lst[0],cpy_lst[i])
        cpy_lst[0]=cpy_lst[0]//n
        cpy_lst[i]=cpy_lst[i]//n
    res.append(str(cpy_lst[0])+"/"+str(cpy_lst[i]))
for i in res:
    print(i)
