# 파일 합치기 : https://www.acmicpc.net/problem/11066

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    
    K = int(input())
    files = list(map(int, input().split()))
    
    
    # 누적합 배열
    _sum = [0] * K
    _sum[0] = files[0]
    for i in range(1, K):
        _sum[i] = _sum[i - 1] + files[i]
    
    # dp[i][j] = i번부터 j번 파일까지 합치는 최소 비용
    dp = [[0] * K for _ in range(K)]
    
    # 파일 길이 2부터 n까지
    for length in range(2, K + 1):      # length: 합칠 구간의 길이
        for i in range(K - length + 1): # 시작점
            j = i + length - 1          # 끝점
            dp[i][j] = float('inf')     # 최소를 찾기 위해 초기값 설정
            
            for k in range(i, j):       # i~j 구간을 [i~k], [k+1~j]로 분할
                # 현재 구간 [i~j]의 총 합 구하기
                total = _sum[j] - (_sum[i - 1] if i > 0 else 0)
                cost = dp[i][k] + dp[k + 1][j] + total
                dp[i][j] = min(dp[i][j], cost)
    
    print(dp[0][K - 1])
    