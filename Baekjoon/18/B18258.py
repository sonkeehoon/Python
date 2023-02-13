import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
N = int(input().strip())
for _ in range(N):
    cmd = input().strip().split()
    c = cmd[0]
    if c == 'push':
        queue.append(cmd[1])
    elif c == 'pop':
        if queue:
            print(queue.popleft())
            continue
        print(-1)
    elif c == 'size':
        print(len(queue))
    elif c == 'empty':
        if queue:
            print(0)
            continue
        print(1)
    elif c == 'front':
        if queue:
            print(queue[0])
            continue
        print(-1)
    elif c == 'back':
        if queue:
            print(queue[-1])
            continue
        print(-1)
        
        
        