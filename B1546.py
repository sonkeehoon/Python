N=int(input())
lst=[]
lst=list(map(int,input().split(" ")))
M=max(lst)
for i in range(N):
    lst[i]=(lst[i]/M)*100
print((sum(lst))/N)