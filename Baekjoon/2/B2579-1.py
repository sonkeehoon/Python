import sys
input = sys.stdin.readline
N = int(input())
X = [int(input()) for _ in range(N)]

def solution(N, X):
    
    if N == 1 or N == 2:
        return sum(X[:N])
    
    dp = [0 for _ in range(N)]
    dp[0] = X[0]
    dp[1] = X[0] + X[1]
    dp[2] = max(X[0] + X[2], X[1] + X[2])
    
    for i in range(3, N):
        dp[i] = max(dp[i - 3] + X[i - 1], dp[i - 2]) + X[i]  # 점화식
    
    return dp[-1]

print(solution(N, X))
    