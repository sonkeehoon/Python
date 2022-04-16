M=int(input())
N=int(input())
lst=[]
for i in range(M,N+1):
    if i==1:
        continue
    lst.append(i)
    for j in range(2,i):
        if i%j==0:
            lst.pop(-1)
            break
if len(lst)==0:
    print(-1)
else:
    print(sum(lst),min(lst),sep="\n")