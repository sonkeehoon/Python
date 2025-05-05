# 행렬 곱셈: https://www.acmicpc.net/problem/10830
import sys
input = sys.stdin.readline


def matrix_multiply(m1, m2, n): # n x n 인 두 행렬의 곱셈을 구해주는 함수
    
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += m1[i][k] * m2[k][j]
            res[i][j] = tmp % 1000
    
    return res
    
def divide_and_conquer(matrix, b, n):   # 분할 정복

    if b == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix[i][j] % 1000
        return matrix
    
    part = divide_and_conquer(matrix, b//2, n)
    if b % 2 == 0:
        return matrix_multiply(part, part, n)
    else:
        return matrix_multiply(matrix_multiply(part, part, n), matrix, n)


n, b = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
res = divide_and_conquer(matrix, b, n)

for line in res:
    print(*line)