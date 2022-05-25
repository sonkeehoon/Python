import sys
input=sys.stdin.readline
W,H,X,Y,P=map(int,input().split())
cnt=0
R=H/2
for i in range(P):
    x,y=map(int,input().split())
    if X<=x<=X+W and Y<=y<=Y+H:
        cnt+=1
        continue
    elif (x-X)**2+(y-(Y+R))**2<=R**2 or (x-(X+W))**2+(y-(Y+R))**2<=R**2:
        cnt+=1 
    continue
print(cnt)