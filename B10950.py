N=int(input())
sum=[_ for _ in range(N)]
for i in range(0,N):
    a,b=map(int,input().split(" "))
    sum[i]=a+b
for j in range(0,N):
    print(sum[j])