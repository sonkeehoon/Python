# 동전 1 : https://www.acmicpc.net/problem/2293
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))      # 입력 받기

dp = [1] + [0] * k                  # dp 리스트 초기화

for coin in coins:                  # coins에 담긴 coin을 하나씩 순회
    for i in range(coin, k + 1):    
        dp[i] += dp[i - coin]

print(dp[-1])