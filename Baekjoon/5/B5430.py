# AC : https://www.acmicpc.net/problem/5430
# 스스로 해결 여부 : X
# 쉬워 보였으나 생각보다 어려웠다
# 처음에는 시간초과가 떴다 f==R일때마다 reverse를 해서였다
# 그래서 R함수의 횟수를 revcount 변수에 담아두고
# D함수에서는 revcount가 짝수인지 홀수인지에 따라 분기를 나눴다
# 그리고 마지막에 출력할때도 홀수일때만 뒤집어줘서 reverse 횟수를 최소화 했다

import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T) :
    tmp = True
    p = input().rstrip()
    n = int(input())
    x = deque(input().strip('\n[]').split(','))
    if x == deque(['']):
        x = deque()
    revcount = 0
    
    for f in p:
        if f == "R":
            revcount += 1
        elif x and f == "D": # x가 비어있지 않고 함수가 D면
            if revcount % 2 == 0:
                x.popleft()
            else:
                x.pop()
        else:
            print("error")
            tmp = False
            break
    
    if tmp:
        if revcount % 2 == 1:
            x.reverse()
        print("["+",".join(x)+"]")
        
            
                
    

            
    