# 동전 2 : https://www.acmicpc.net/problem/2294
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] + [float("inf") for _ in range(k)]      # dp 리스트 초기화

for coin in coins:                  # coins에 담긴 coin을 하나씩 순회
    for i in range(coin, k + 1):
        dp[i] = min(dp[i - coin] + 1, dp[i])
    
# if dp[-1] == float("inf"):
#     print(-1)
# else:
#     print(dp[-1])

print(-1 if dp[-1] == float("inf") else dp[-1])