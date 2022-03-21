h,m=map(int,input().split(" "))
t=int(input())


if h+(m+t)//60>=24:
    print(h+((m+t)//60-24),(m+t)%60)
else :
    print(h+(m+t)//60,(m+t)%60)
    
    
    





           