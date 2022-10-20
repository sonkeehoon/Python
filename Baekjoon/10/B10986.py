import sys
input=sys.stdin.readline
N,M=map(int,input().split())
lst=[0]+list(map(int,input().split()))
m,res=[0],0
rem=[0]*M
rem[0]=1
for i in range(1,N+1):
    lst[i]=(lst[i-1]+lst[i])%M
    rem[lst[i]]+=1
for i in range(M):
    res+=rem[i]*(rem[i]-1)//2
print(res)
    