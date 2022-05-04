import sys
import math
input=sys.stdin.readline
N=int(input())
lst=[int(input()) for i in range(N)]
res=[]
lst.sort()
gcd=lst[1]-lst[0]
for i in range(2,N):
    gcd=math.gcd(gcd,lst[i]-lst[i-1])
res=[]
for i in range(2,int(math.sqrt(gcd))+1):
    if gcd%i==0:
        res.append(i)
        res.append(gcd//i)
res.append(gcd)
res=list(set(res))
res.sort()
for i in res:
    print(i,end=' ')
