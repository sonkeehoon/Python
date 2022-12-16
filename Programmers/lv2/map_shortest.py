# 게임 맵 최단거리 : https://school.programmers.co.kr/learn/courses/30/lessons/1844
# deque와 bfs
# 어렵다.. 이걸 혼자 생각해낼수 있다면 참 기쁘겠다
from collections import deque
def solution(maps):
    # maps : 지도, answer : 최단거리
    # (1,1) -> (5,5) 경로
    # maps에서 0은 벽, 1은 길
    answer = 0
    n, m = len(maps), len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0,0)])
    
    while queue:
        x, y = queue.popleft()
        
        # 상하좌우 4방향 확인
        for i in range(4): # 우 : (-1, 0) 좌 : (1, 0) 하 : (0, -1) 상 : (0, 1)
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵을 벗어나거나 길이 아니면 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] != 1:
                continue
            
            maps[nx][ny] = maps[x][y] + 1 
            queue.append((nx,ny))
            print(queue)
            
    answer = maps[-1][-1]
    if answer > 1:
        return answer
    return -1
    
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))