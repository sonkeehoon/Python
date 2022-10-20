A,B,C=map(int,input().split(" "))
i=1
if B<C:
    d=A//(C-B)
    if d>=0:
        print(d+1)
else : print(-1)

