import sys
T=int(sys.stdin.readline())
for _ in range(T):
    x,y=map(int,sys.stdin.readline().split())
    lst=[]
    for i in range(1,min(x,y)+1):
        if x%i==0 and y%i==0:
            lst.append(i)
    print(x*y//max(lst))