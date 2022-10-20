x,y=[0]*3,[0]*3
for i in range(3):
    x[i],y[i]=map(int,input().split())
x.sort()
y.sort()
rx,ry=0,0
if x[1]==x[0]:
    rx=x[2]
else:
    rx=x[0]
if y[1]==y[0]:
    ry=y[2]
else:
    ry=y[0]
print(rx,ry)
