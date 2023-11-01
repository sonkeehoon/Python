# 스택 2 : https://www.acmicpc.net/problem/28279
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

stack = deque()
for _ in range(N):
    cmd = input()
    type = cmd[0]
    if type == "1":
        X = int(cmd[2:])
        stack.append(X)
        
    elif type == "2":
        if stack:
            print(stack.pop())
            continue
        print(-1)
    
    elif type == "3":
        size = len(stack)
        print(size)
    
    elif type == "4":
        if stack:
            print(0)
            continue
        print(1)
    
    elif type == "5":
        if stack:
            print(stack[-1])
            continue
        print(-1)