from itertools import combinations_with_replacement as cwr
N,M=map(int,input().split())
lst=[str(i) for i in range(1,N+1)]
for i in cwr(lst,M):
    print(' '.join(i))