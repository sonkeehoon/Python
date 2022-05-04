from math import factorial as fact
T=int(input())
for i in range(T):
    x,y=map(int,input().split())
    print(fact(y)//(fact(x)*fact(y-x)))

