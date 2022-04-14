N=int(input())
lst=map(int,input().split())
cnt=N
for i in lst:
    if i==1:
        cnt-=1
    for j in range(2,i):
        if i%j==0:
            cnt-=1
            break
print(cnt)