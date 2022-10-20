h,m=map(int,input().split(" "))
if m>=45:
    print(h,m-45)
elif m<45 and h!=0:
    print(h-1,m+15)
if m<45 and h==0:
    print(23,m+15)