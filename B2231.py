N=int(input())
res=[]
for i in range(N):
    numlist=list(map(int,str(i)))
    if sum(numlist)+i==N:
        res.append(i)
if len(res)==0: print(0)
else: print(min(res))