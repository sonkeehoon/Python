from math import factorial as fact
N,K=map(int,input().split())
comb=lambda n,r: fact(n)//(fact(n-r)*fact(r))
print(comb(N,K))