# 스도쿠: https://www.acmicpc.net/problem/2580
'''
1. 각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
2. 굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
'''
import sys
input = sys.stdin.readline
size = 9

def solve(idx):
    
    if idx == len(empty):
        for row in board:
            print(*row)
        sys.exit(0)
    
    x, y = empty[idx]
    box = (x//3)*3 + (y//3)
    
    for num in range(1, 10):
        if not row_used[x][num] and not col_used[y][num] and not box_used[box][num]:  # 가능한 값이면
            board[x][y] = num
            row_used[x][num] = col_used[y][num] = box_used[box][num] = True
        
            solve(idx + 1)
            
            board[x][y] = 0
            row_used[x][num] = col_used[y][num] = box_used[box][num] = False
            

board = [list(map(int, input().split())) for _ in range(size)]

# 각 행, 열, 박스에 어떤 숫자가 쓰였는지 기억할 표
row_used = [[False]*10 for _ in range(9)]  # [행][숫자]
col_used = [[False]*10 for _ in range(9)]  # [열][숫자]
box_used = [[False]*10 for _ in range(9)]  # [박스][숫자]

empty = []  # 비어있는 칸의 좌표들

for i in range(size):
    for j in range(size):
        num = board[i][j]
        if num == 0:  # 비어있으면
            empty.append((i, j))
        else:
            row_used[i][num] = True
            col_used[j][num] = True
            box_used[(i//3)*3 + (j//3)][num] = True

solve(0)
