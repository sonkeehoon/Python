import sys
input=sys.stdin.readline
N=int(input())
lst=[]
dp=[0 for i in range(N)]
for _ in range(N):
    lst.append(int(input()))
if N==1:
    print(lst[0])
    exit()
elif N==2:
    print(max(lst[0]+lst[1],lst[1]))
    exit()
dp[0]=lst[0]
dp[1]=max(lst[1],lst[0]+lst[1])
dp[2]=max(lst[0]+lst[2],lst[1]+lst[2])
for i in range(3,N):
    dp[i]=max(dp[i-2]+lst[i],dp[i-3]+lst[i-1]+lst[i])
print(dp[-1])
