# 3 x n 타일링 : https://school.programmers.co.kr/learn/courses/30/lessons/12902#

def solution(n):
    dp = [1,0,3,0]
    N = 10**9 + 7
    
    for i in range(4,n+1):
        if i % 2 == 1:
            dp.append(0)
            continue
        x = 4 * dp[i-2]
        y = dp[i-4]
        dp.append(((x%N-y%N)+N)%N)
        
    return dp[n]
