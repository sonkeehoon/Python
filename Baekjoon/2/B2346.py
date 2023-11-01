# 풍선 터뜨리기 : https://www.acmicpc.net/problem/2346
import sys
from collections import deque
input = sys.stdin.readline

# 양수는 오른쪽, 음수는 왼쪽
N = int(input())
balloons = list(map(int,input().split()))
q = deque([(value, idx+1) for idx,value in enumerate(balloons)]) # (풍선의 값, 풍선의 번호)를 튜플로 묶는다
res = []
while q:
    (v,i) = q.popleft()
    res.append(i)
    if v > 0:
        q.rotate(1-v)
    else:
        q.rotate(-v)

print(*res)
    

    