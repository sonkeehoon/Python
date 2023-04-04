# 영단어 암기는 괴로워 : https://www.acmicpc.net/problem/20920
# 스스로 해결 여부 : O
# 딕셔너리와 get함수로 풀었다
# 다중 정렬을 공부할수 있는 문제

import sys
from collections import Counter
input = sys.stdin.readline

N,M = map(int,input().split())

d = {}
for _ in range(N):
    s = input().rstrip()
    if len(s) >= M:
        if d.get(s) == None: # 처음 들어오는 key값이면
            d[s] = 1
        else:
            d[s] += 1
# d = dict(sorted(d.items(), key = lambda x : (-x[1], -len(x[0]),x[0]), reverse=False)) # 이 방식은 한줄이라 깔끔해 보이지만 메모리나 시간이 비효율적
# 귀찮더라도 한줄에 하나씩 정렬하자(정렬 중요도를 역순으로)
# 제출은 내가 짠 코드로 했다 그런데
# dict 대신 Counter를 쓰고 정렬은 lst로만 해서 시간,메모리를 많이 절약한 다른사람 코드를 보고 신기했다
# 다른사람 코드 : https://www.acmicpc.net/source/58716088

d = dict(sorted(d.items() , key = lambda x:x[0])) # 
d = dict(sorted(d.items() , key = lambda x:len(x[0]),reverse=True))
d = dict(sorted(d.items() , key = lambda x:x[1],reverse=True))
print(*d,sep='\n')

