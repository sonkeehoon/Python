# from itertools import combinations as comb
# N,M=map(int,input().split())
# lst=[str(i) for i in range(1,N+1)]
# for i in comb(lst,M):
#     print(' '.join(i))
# 모듈 쓰지않고
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
lst=[]
def combination(s):
    if len(lst)==M:
        print(*lst)
        return
    for i in range(s,N+1):
        if i not in lst:
            lst.append(i)
            combination(i)
            lst.pop()
combination(1)