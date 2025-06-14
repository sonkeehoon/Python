# 두 수의 합 : https://www.acmicpc.net/problem/3273
import sys
input = sys.stdin.readline
n = int(input()) # len(arr)
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
res = set()

i, j = 0, n - 1 # (0 <= i < j <= n)
sum_ = arr[i] + arr[j]

while i < j:
    
    if sum_ == x:
        res.add((arr[i], arr[j]))
        i += 1
        j -= 1
        sum_ += arr[i] - arr[i - 1]
        sum_ -= arr[j + 1] - arr[j]
            
        
    elif sum_ < x:
        i += 1
        sum_ += arr[i] - arr[i - 1]
        
    elif sum_ > x:
        j -= 1
        sum_ -= arr[j + 1] - arr[j]

print(len(res))

