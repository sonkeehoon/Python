# 부분합: https://www.acmicpc.net/problem/1806
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
p_sum = 0
min_len = float("inf")

while True:
    
    if p_sum < s:
        if right + 1 < n:
            right += 1
            p_sum += arr[right]
        else:
            break

    elif p_sum >= s:
        if left < right:
            min_len = min(min_len, right - left + 1)
            p_sum -= arr[left]
            left += 1
        
        elif left == right:
            min_len = min(min_len, right - left + 1)
            right += 1
            
        elif left > right:
            right += 1
            
print(0 if min_len == float("inf") else min_len)
