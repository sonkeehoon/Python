import sys
size = 9
input = sys.stdin.readline
matrix = [list(map(int,input().split())) for _ in range(size)]
# for i in range(size):
#     matrix.append(list(map(int,input().split())))

# 최댓값 탐색
temp = []
for row in matrix:
    temp.append(max(row))
target = max(temp)

# 최댓값의 인덱스 탐색
for i in range(size):
    for j in range(size):
        if matrix[i][j] == target:
            print(target)
            print(i+1, j+1)
            exit()
    