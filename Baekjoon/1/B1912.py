# 연속합: https://www.acmicpc.net/problem/1912
import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = s[0]
_sum = s[0]
for i in range(1, len(s)):
    if _sum < 0 :
       _sum = 0
    _sum += s[i]
    dp[i] = max(dp[i - 1], _sum)

print(max(dp))
    