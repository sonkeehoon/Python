import sys
input=sys.stdin.readline
N,M=map(int,input().split())
lst=list(map(int,input().split()))
sum_lst=[0]*N
sum_lst[0]=lst[0]
for i in range(1,N):
    sum_lst[i]=sum_lst[i-1]+lst[i]
for i in range(M):
    x,y=map(int,input().split())
    if x==1:
        print(sum_lst[y-1])
        continue
    print(sum_lst[y-1]-sum_lst[x-2])