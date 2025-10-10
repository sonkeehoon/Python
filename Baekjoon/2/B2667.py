# 단지번호붙이기: https://www.acmicpc.net/problem/2667
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

houses = [list(map(int, input().strip())) for _ in range(N)]
group = 0
res = []
visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        
        if not visited[i][j] and houses[i][j] == 1:
            visited[i][j] = True
            group += 1
            cnt = 1
            houses[i][j] = group
            q = deque()
            q.append((i, j))
            direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            
            while q:
                idx_i, idx_j = q.popleft()
                
                for dx, dy in direction:
                    next_x = idx_i + dx
                    next_y = idx_j + dy
                    
                    if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N: # 범위를 벗어나면
                        continue
                    
                    if not visited[next_x][next_y] and houses[next_x][next_y] == 1:
                        visited[next_x][next_y] = True
                        houses[next_x][next_y] = group
                        cnt += 1
                        q.append((next_x, next_y))
            res.append(cnt)
                    
print(len(res))
res.sort()
for i in range(len(res)):
    print(res[i])
                        
                             
                
                
                
                
             
            
        
