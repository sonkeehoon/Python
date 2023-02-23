import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    q = deque(map(int,input().split()))
    cnt = 0
    if max(q) == q[0]:
        q.popleft()
        
    