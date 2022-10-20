N=int(input())
A=list(map(int,input().split()))
dp=[0]*N
revA=list(reversed(A))
for i in range(N):
    temp=0
    for j in range(i):
        if A[i]>A[j]:
            temp=max(temp,dp[j])
    dp[i]=temp+1
revDp=[0]*N
for i in range(N):
    temp=0
    for j in range(i):
        if revA[i]>revA[j]:
            temp=max(temp,revDp[j])
    revDp[i]=temp+1
revDp=list(reversed(revDp))
res=[x+y-1 for x,y in zip(dp,revDp)]
print(max(res))