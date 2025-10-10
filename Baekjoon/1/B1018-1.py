# 체스판 다시 칠하기: https://www.acmicpc.net/problem/1018
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

board = [input().strip() for _ in range(N)]
size = 8
res = 65

for i in range(N - 7):
    for j in range(M - 7):
        cnt1, cnt2 = 0, 0
        first1, second1 = 'W', 'B'
        for k in range(8):
            for l in range(8):
                cur = board[k + i][l + j]
                if (k + l) % 2 == 0:
                    if cur != first1:
                        cnt1 += 1
                    if cur != second1:
                        cnt2 += 1
                    
                elif (k + l) % 2 == 1:
                    if cur != second1:
                        cnt1 += 1
                    if cur != first1:
                        cnt2 += 1
                
        res = min(res, cnt1, cnt2)

print(res)
                    

                
                
                
            
                    
                
            