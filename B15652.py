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
def cwr():
    global lst
    if len(lst)==M:
        print(*lst)
        return
    for i in range(1,N+1):
        if len(lst)!=0 and i<lst[-1]:
            continue
        lst.append(i)
        cwr()
        lst.pop()
cwr()