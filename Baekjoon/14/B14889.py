# 스타트와 링크: https://www.acmicpc.net/problem/14889
import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

start_lst = list(combinations(range(N), N // 2))
num = len(start_lst) // 2
ans = float('inf')

for i in range(num):
    start = start_lst[i]
    link = list(set(range(N)) - set(start))
    start_sum, link_sum = 0, 0
    
    start_stat = list(combinations(start, 2))
    link_stat = list(combinations(link, 2))
    start_sum = sum(S[x][y] + S[y][x] for x, y in start_stat)
    link_sum = sum(S[x][y] + S[y][x] for x, y in link_stat)
    ans = min(abs(link_sum - start_sum), ans)

print(ans)
