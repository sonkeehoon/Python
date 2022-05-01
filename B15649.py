from itertools import permutations as perm
N,M=map(int,input().split())
lst=[str(i) for i in range(1,N+1)]
for i in perm(lst,M):
    print(' '.join(i))