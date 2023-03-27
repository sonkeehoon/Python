# 하루 종일 고민했는데 결국 혼자서는 못풀었다
# 다음날 구글링해서 dp로 깔끔하게 푸는사람을 보고 감탄했다
# 최장 공통수열(LIS)로 푸는 문제였다(혼자는 절대 생각 못해낼듯)
# 익숙해지는 과정이라고 생각하자(이런 문제들 풀다보면 이해되겠지)
# 2차원 리스트에 sort함수를 쓰면 

import sys
input = sys.stdin.readline
n = int(input())
arr = []
dp = [1 for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()

for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
    
    
