import sys
input = sys.stdin.readline
size = 100
paper = 10
square = [[0 for _ in range(size)] for _ in range(size)]
n = int(input())
for _ in range(n):
    x, y = map(int,input().split())
    for i in range(x, paper + x):
        for j in range(y, paper + y):
            square[i][j] = 'B'
cnt = 0
for row in square:
    cnt += row.count('B')

print(cnt)
    

            
    
    
    
    