# N*M 크기의 두 행렬 A, B
N, M = map(int,input().split())

A, B = [], []
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    B.append(list(map(int,input().split())))
res = []
for i in range(N):
    line = []
    for j in range(M):
        line.append(A[i][j] + B[i][j])
    res.append(line)
for row in res:
    print(*row)
        