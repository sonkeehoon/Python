from itertools import combinations as comb
N,M=map(int,input().split())
lst=[str(i) for i in range(1,N+1)]
for i in comb(lst,M):
    print(' '.join(i))