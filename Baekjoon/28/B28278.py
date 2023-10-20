# 스택 2 : https://www.acmicpc.net/problem/28278
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

stack = deque()
for _ in range(N):
    cmd = input()
    if cmd[0] == "1":
        X = int(cmd[2:])
        stack.append(X)
        
    elif cmd[0] == "2":
        if stack:
            print(stack.pop())
            continue
        print(-1)
    
    elif cmd[0] == "3":
        size = len(stack)
        print(size)
    
    elif cmd[0] == "4":
        if stack:
            print(0)
            continue
        print(1)
    
    elif cmd[0] == "5":
        if stack:
            print(stack[-1])
            continue
        print(-1)