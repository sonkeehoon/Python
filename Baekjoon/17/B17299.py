# 오등큰수 : https://www.acmicpc.net/problem/17299
# 스스로 해결 여부 : 
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
F = Counter(A)
tmp, res = [], [-1]
x = A.pop()
tmp.append(x)

while A:
    x = A.pop()
    tmp.append(x)
    if F[tmp[-1]] < F[tmp[-2]]:
        y = tmp[-2]
    elif F[tmp[-1]] > F[tmp[-2]]: # 검색
        y = -1
        for i in range(-2, -len(tmp)-1, -1):
            if tmp[-1] > tmp[i]:
                y = tmp[i]
                break
                
    elif F[tmp[-1]] == F[tmp[-2]]:
        y = res[-1]
    
    res.append(y)

print(*res[::-1])
        
        