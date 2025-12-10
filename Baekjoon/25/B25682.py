# 체스판 다시 칠하기 2: https://www.acmicpc.net/problem/25682
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [input().strip() for _ in range(N)]

# ps[i][j] : (0,0) ~ (i-1, j-1) 구간에서
# "왼쪽 위가 B인 체스판" 패턴과 다른 칸의 개수 (mismatch 수)
ps = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N):
    row = board[i]
    psi = ps[i]
    psi1 = ps[i + 1]
    for j in range(M):
        # (i + j)가 짝수이면 B, 홀수이면 W가 와야 하는 패턴
        expected = 'B' if (i + j) % 2 == 0 else 'W'
        mismatch = 1 if row[j] != expected else 0

        # 2차원 누적합
        psi1[j + 1] = psi1[j] + psi[j + 1] - psi[j] + mismatch

ans = 10**9
KK = K * K

# (i, j)를 KxK 부분보드의 "오른쪽 아래" 좌표로 본다 (1-indexed 기준)
for i in range(K, N + 1):
    psi = ps[i]
    psiK = ps[i - K]
    for j in range(K, M + 1):
        # B 시작 패턴으로 만드는 데 필요한 repaint 수
        repaintB = (
            psi[j]
            - psiK[j]
            - psi[j - K]
            + psiK[j - K]
        )
        
        # W 시작 패턴으로 만드는 비용은 K*K - repaintB
        repaint = repaintB if repaintB <= KK - repaintB else KK - repaintB

        if repaint < ans:
            ans = repaint

print(ans)
