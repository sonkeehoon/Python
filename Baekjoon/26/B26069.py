# 붙임성 좋은 총총이 : https://www.acmicpc.net/problem/26069
# https://upload.acmicpc.net/12d3d8d8-06c0-4b31-b661-0ce1bc935cf9/-/preview/
# https://upload.acmicpc.net/4efdc327-804f-4929-8b6f-5b85577135c8/-/preview/
# set에 데이터를 여러개 넣을때는 add보다 update를 활용하면 좋다 (중복되는 원소는 알아서 제거해준다)
# 1개의 값을 넣을때는 add만 가능하다 (update로 1개의 값을 넣으려고 하면 error 발생)
# 처음에 set으로 접근했다가 문제를 제대로 이해하고 defaultdict로 다시 풀었다
# 마지막에 다시 set으로 풀었다. 이게 가장 효율적인 코드같다

import sys
input = sys.stdin.readline

dance = {'ChongChong'}
for _ in range(int(input())):
    x,y = input().split()
    if x in dance or y in dance: dance.update((x,y))
    
print(len(dance))
    
        
        
    