N=int(input())
lst=[0,1,2]
for i in range(3,N+1):
    lst.append((lst[i-2]+lst[i-1])%15746)
print(lst[N]%15746)


