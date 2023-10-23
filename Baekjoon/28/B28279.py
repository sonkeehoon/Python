# 덱 2 : https://www.acmicpc.net/problem/28278
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

queue = deque()
for _ in range(N):
    cmd = input()
    type = cmd[0]
    if type == "1":
        X = int(cmd[2:])
        queue.append(X)
    elif type == "2":
        X = int(cmd[2:])
        queue.appendleft(X)
    elif type == "3":
        if queue:
            print(queue.pop())
            continue
        print(-1)
    elif type == "4":
        if queue:
            print(queue.popleft())
            continue
        print(-1)
    elif type == "5":
        print(len(queue))
    elif type == "6":
        if queue:
            print(0)
            continue
        print(1)
    elif type == "7":
        if queue:
            print(queue[-1])
            continue
        print(-1)
    elif type == "8":
        if queue:
            print(queue[0])
            continue
        print(-1)