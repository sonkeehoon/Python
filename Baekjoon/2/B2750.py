N=int(input())
lst=[]
for _ in range(N):
    lst.append(int(input()))
res=[0]*N
for i in range(N):
    cnt=0
    for j in range(N):
        if lst[i]>lst[j]:
            cnt+=1
    res[cnt]=lst[i]
for i in res:
    print(i)
