# from itertools import product
# N,M=map(int,input().split())
# lst=[str(i) for i in range(1,N+1)]
# for i in product(lst,repeat=M):
#     print(' '.join(i))
# 모듈 쓰지않고
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
lst=[]
def product():
    if len(lst)==M:
        print(*lst)
        return
    for i in range(1,N+1):
        lst.append(i)
        product()
        lst.pop()
product()