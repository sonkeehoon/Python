T=int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
            continue
    d=((x1-x2)**2)+((y1-y2)**2)
    dr=abs(r2-r1)
    range=(r1+r2)**2
    if d==dr**2 or d==range:
        print(1)
    elif d>range or d<dr**2:
        print(0)
    else:
        print(2)