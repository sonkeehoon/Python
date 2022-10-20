# 모듈 쓰고
# from itertools import permutations as perm
# N,M=map(int,input().split())
# lst=[str(i) for i in range(1,N+1)]
# for i in perm(lst,M):
#     print(' '.join(i))

# 모듈 쓰지않고
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
lst=[]
def permutation():
    if len(lst)==M:
        print(*lst)
        return
    for i in range(1,N+1):
        if i not in lst:
            lst.append(i)
            permutation()
            lst.pop()
permutation()