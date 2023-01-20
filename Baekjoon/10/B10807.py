import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int,input().split()))
v = int(input())
# print(lst.count(v))
cnt = 0
for l in lst:
    if l == v:
        cnt += 1
print(cnt)
