# 좌표 압축: https://www.acmicpc.net/problem/18870
# 정렬 풀이(효율 좋음)
import sys
input = sys.stdin.readline
n = int(input())
X = list(map(int, input().split()))
set_lst = sorted(list(set(X)))
d = {}

for i, e in enumerate(set_lst):
    d[e] = i

for x in X:
    print(d[x], end=' ')