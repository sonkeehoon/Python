# 붙임성 좋은 총총이 : https://www.acmicpc.net/problem/26069
# https://upload.acmicpc.net/12d3d8d8-06c0-4b31-b661-0ce1bc935cf9/-/preview/
# https://upload.acmicpc.net/4efdc327-804f-4929-8b6f-5b85577135c8/-/preview/
# set에 데이터를 여러개 넣을때는 add보다 update를 활용하면 좋다 (중복되는 원소는 알아서 제거해준다)
# 1개의 값을 넣을때는 add만 가능하다 (update로 1개의 값을 넣으려고 하면 error 발생)
# 처음에 set으로 접근했다가 문제를 제대로 이해하고 defaultdict로 다시 풀었다

import sys
from collections import defaultdict
input = sys.stdin.readline

target = "ChongChong"
dance = defaultdict(int)
cnt = 0
for _ in range(int(input())):
    x,y = input().split()
    if x == target or y == target:
        dance[x], dance[y] = True, True
        continue
    if dance[x] or dance[y]:
        dance[x], dance[y] = True, True

print(dance)
for v in dance.values():
    if v: cnt += 1
print(cnt)
    
        
        
    