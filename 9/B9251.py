A=input()
B=input()
dp=[0]*1000
for i in range(len(A)):
    temp=0
    for j in range(len(B)):
        if temp<dp[j]:
            temp=dp[j]
        elif A[i]==B[j]:
            dp[j]=temp+1
print(max(dp))

# sa,sb=input(),input()
# dp=[0]*1000
# for i in range(len(sa)):
#     MAX=0
#     for j in range(len(sb)):
#         if MAX<dp[j]:
#             MAX=dp[j]
#         elif sa[i]==sb[j]:
#             dp[j]=MAX+1
# print(max(dp))
