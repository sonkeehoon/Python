lst=[]
while True:
    x,y=map(int,input().split())
    if x==y==0:
        break
    elif y%x==0:
        lst.append("factor")
        continue
    elif x%y==0:
        lst.append("multiple")
        continue
    else:
        lst.append("neither")
for i in lst:
    print(i)