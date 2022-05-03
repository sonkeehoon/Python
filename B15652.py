# from itertools import combinations_with_replacement as cwr
# N,M=map(int,input().split())
# lst=[str(i) for i in range(1,N+1)]
# for i in cwr(lst,M):
#     print(' '.join(i))
# 모듈 쓰지않고
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
lst=[]
def cwr(s):
    if len(lst)==M:
        print(*lst)
        return
    for i in range(s,N+1):
        lst.append(i)
        cwr(i)
        lst.pop()
        
cwr(1)