# 부분합: https://www.acmicpc.net/problem/1806
import sys
input = sys.stdin.readline
import time

n, s = map(int, input().split())
arr = list(map(int, input().split()))

i, j = 0, 0
_sum = sum(arr[i:j + 1])
min_len = float("inf")

while i < n:
    time.sleep(0.5)
    print(i, j, _sum, min_len)
    
    if _sum >= s:
        min_len = min(min_len, j - i + 1)
        if i <= j:
            _sum -= arr[i]
            i += 1
    
    elif _sum < s:
  
        if j < n - 1:
            _sum += arr[j + 1]
            j += 1
        elif j == n - 1:
            break

print(0 if min_len == float("inf") else min_len)