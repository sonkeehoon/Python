N=int(input())
lst=[0]*N
lst=list(map(int,input()))
sum = 0
for s in lst:
    sum += s
print(sum)