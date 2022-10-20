from sys import stdin
input=stdin.readline
n=int(input())
lst,dp=[0],[0]*(n+1)
for i in range(n):
    lst.append(int(input())) 
if n==1 :
    print(lst[1])
    exit()
elif n==2:
    print(lst[1]+lst[2])
    exit()
dp[1],dp[2]=lst[1],lst[1]+lst[2]
dp[3]=max(lst[0]+lst[1],lst[0]+lst[2])+lst[3]
for i in range(4,n+1):
    dp[i]=max(dp[i-2],max(dp[:i-2])+lst[i-1])+lst[i]
print(max(dp))