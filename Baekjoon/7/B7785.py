import sys
input = sys.stdin.readline
n = int(input())
d = {}

for _ in range(n):
    name, state = input().split()
    if state == "enter": # 출근 상태면
        d[name] = True
    elif state == "leave":
        del d[name]
print(*sorted(d.keys(), reverse=True), sep='\n')

