# 톱니바퀴: https://www.acmicpc.net/problem/14891
import sys
from collections import deque
input = sys.stdin.readline

circles = [deque(map(int, input().strip())) for _ in range(4)]
rotate_chk = [False] * 3
rotate_queue = deque()
score = 0

# 인접한 두 극이 다를경우 True
def update_rotate_chk(rotate_chk, circles)-> list:
    for i in range(3):
        if circles[i][2] != circles[i + 1][6]:
            rotate_chk[i] = True
        else:
            rotate_chk[i] = False
            
    return rotate_chk

K = int(input())
for _ in range(K):
    
    rotate_chk = update_rotate_chk(rotate_chk, circles)
    circle, direction = map(int, input().split())
    rotate_queue.append((circle - 1, direction))
    visited = [False] * 4
    visited[circle - 1] = True
    
    while rotate_queue:
        cur_circle, cur_dir = rotate_queue.popleft()
        circles[cur_circle].rotate(cur_dir)
        
        if cur_circle > 0:
            if not visited[cur_circle - 1] and rotate_chk[cur_circle - 1]:
                visited[cur_circle - 1] =  True
                rotate_queue.append((cur_circle - 1, -cur_dir))
        
        if cur_circle < 3:
            if not visited[cur_circle + 1] and rotate_chk[cur_circle]:
                visited[cur_circle + 1] = True
                rotate_queue.append((cur_circle + 1, -cur_dir))

for i in range(len(circles)):
    if circles[i][0] == 1:  # S극 이면
        score += 2**i
        
print(score)

