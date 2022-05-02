from itertools import product
N,M=map(int,input().split())
lst=[str(i) for i in range(1,N+1)]
for i in product(lst,repeat=M):
    print(' '.join(i))