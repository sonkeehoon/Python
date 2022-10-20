import sys
input=sys.stdin.readline
n=int(input())
lst=[]
for i in range(n):
    lst.append(list(map(int,input().split())))
dp=[[0]*(i+1) for i in range(n)]
dp[0][0]=lst[0][0]
for i in range(1,n):
    dp[i][0]=dp[i-1][0]+lst[i][0]
    dp[i][i]=dp[i-1][i-1]+lst[i][i]
    if i==1:
        continue
    for j in range(1,i):
        dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+lst[i][j]
print(max(dp[n-1]))
    