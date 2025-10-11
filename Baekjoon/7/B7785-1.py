# 회사에 있는 사람: https://www.acmicpc.net/problem/7785
import sys
input = sys.stdin.readline
n = int(input())
d = {}

for _ in range(n):
    name, tmp = input().split()
    if tmp == 'enter':
        d[name] = tmp
    elif tmp == 'leave':
        del d[name]

print(*sorted(d.keys(), reverse = True), sep= '\n')
    