from math import factorial as fact

def solution(n):
    answer = 0
    div = 1234567
    dp = [1,2]
    if n == 1 or n == 2:
        return dp[n-1]
    
    for i in range(2,n):
        dp.append(dp[i-1] + dp[i-2])
    answer = dp[n-1]
    return answer%div