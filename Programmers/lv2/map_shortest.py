# 게임 맵 최단거리 : https://school.programmers.co.kr/learn/courses/30/lessons/1844
# deque와 bfs
# 어렵다.. 이걸 혼자 생각해낼수 있다면 참 뿌듯하겠다
from collections import deque
def bfs(start, maps):
    # maps : 지도, answer : 최단거리
    # (1,1) -> (5,5) 경로
    # maps에서 0은 벽, 1은 길
    dirs = [[0,1], [1,0], [0,-1], [-1,0]]
    q = deque()
    q.append(start)
    print(start, q)
    print(len(maps),len(maps[0]))
    
    
    while q: # q가 비어있으면 while문 종료
        y, x, cnt = q.popleft()
        maps[y][x] = 0
        for dy, dx in dirs: # 점마다 4방향 탐색
            print(f"(y,x) = ({y},{x})")
            ny, nx = y + dy, x + dx
            print(q)
            # 다음 지점이 목적지면 cnt+1을 반환
            if ny == len(maps)-1 and nx == len(maps[0])-1 : 
                print("목적지 입니다.")
                return cnt + 1
            # 다음 지점이 목적지가 아니고 벽이 아닌 길일 때
            elif 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == 1 :
                # 지나간 점은 0(벽)으로 만든다
                maps[ny][nx] = 0
                q.append([ny, nx, cnt + 1])
    
    return -1
    
def solution(maps):
    return bfs([0,0,1], maps)
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))