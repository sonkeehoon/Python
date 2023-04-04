# 회전하는 큐 : https://www.acmicpc.net/problem/1021
# 스스로 해결 여부 : O
# 스스로 풀기는 했는데 코딩하기 전에 문제를 이해하기까지 시간이 좀 걸렸다(문해력 이슈)

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split()) # M <= N 
# N은 큐의 크기, M은 뽑아내려고 하는 원소의 갯수
q = deque([i+1 for i in range(N)])
lst = list(map(int,input().split()))

tmp = 0
for i in lst:
    idx = q.index(i)
    if idx == 0:
        q.popleft()
        continue
    size = len(q)
    tmp += min(idx, size-idx)
    q.rotate(-idx)
    q.popleft()
print(tmp)
        
    
            
    
    