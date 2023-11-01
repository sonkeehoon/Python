# queuestack : https://www.acmicpc.net/problem/24511
import sys
from collections import deque
input = sys.stdin.readline
N = int(input()) # A의 길이
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = int(input()) # queuestack에 삽입할 C의 길이
C = list(map(int,input().split()))
q, res = deque(), []
for i in range(len(B)):
    if not A[i]:
        q.append(B[i])
for c in C:
    if not q:
        res = C
        break
    res.append(q.pop())
    q.appendleft(c)
print(*res)
        