# 크로아티아 알파벳: https://www.acmicpc.net/problem/2941
import sys
input = sys.stdin.readline

s = input().strip()
d = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in range(len(d)):
    if d[i] in s:
        s = s.replace(d[i], "#")

print(len(s))