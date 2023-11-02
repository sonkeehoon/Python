# 도키도키 간식드리미 : https://www.acmicpc.net/problem/12789
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
student = deque(map(int,input().split())) # queue
tmp = deque([0]) # stack
now = 1

while student:
    if student[0] == now:
        now += 1
        student.popleft()
    elif tmp[-1] == now:
        now += 1
        tmp.pop()
    else: tmp.append(student.popleft())
    
while tmp:
    if tmp[-1] == now:
        now += 1
        tmp.pop()
        continue
    break

if tmp == deque([0]): print("Nice")
else: print("Sad")
    
        
        
    



