# 색종이 만들기 : https://www.acmicpc.net/problem/2630
"""
각 정사각형은 하얀색 or 파란색
1: 파란색
0: 하얀색

전체 종이 크기는 NxN (N = 2**k, 1 <= k <= 7)

종이를 4등분으로 나누는데 조건은 다음과 같다
- 나누어진 4개의 종이가 모두 같은색으로 나눠져 있지 않은 경우

잘라진 종이가 모두 하얀색(0) 또는 모두 파란색(1) 이거나,
하나의 정사각형 칸이 되어 더이상 자를수 없을 때까지 반복

입력 : 
종이의 한변의 길이 N
NxN 이차원 배열

출력 : 
잘라진 하얀색 색종이 개수
잘라진 파란색 색종이의 개수

"""

import sys
input = sys.stdin.readline
N = int(input())

zero, one = 0, 0
paper = [list(map(int, input().split())) for _ in range(N)]

def is_same(q, N):
    tmp = q[0][0]
    for i in range(N):
        for j in range(N):
            if q[i][j] != tmp:
                return False
    
    return True       

def divide(paper: list, N: int):
    global zero, one
    
    if is_same(paper, N) or len(paper) == 1: # 재귀 종료 조건
        if paper[0][0] == 0:
            zero += 1
        elif paper[0][0] == 1:
            one += 1
        return 
            
    q1 = [[paper[i][j] for i in range(N//2)] for j in range(N//2)]
    q2 = [[paper[i][j] for i in range(N//2)] for j in range(N//2, N)]
    q3 = [[paper[i][j] for i in range(N//2, N)] for j in range(N//2)]
    q4 = [[paper[i][j] for i in range(N//2, N)] for j in range(N//2, N)]
    
    divide(q1, N//2)
    divide(q2, N//2)
    divide(q3, N//2)
    divide(q4, N//2)

divide(paper, N)
print(zero, one)
