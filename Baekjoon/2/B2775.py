import sys
def apart(k,n):
    k+=1
    res1=[]
    for i in range(k):
        line=[]
        for j in range(n):
            line.append(0)
        res1.append(line)
    res1[0]=[_ for _ in range(1,n+1)]
    for i in range(k):
        res1[i][0]=1
    for i in range(1,k):
        for j in range(1,n):
            res1[i][j]=sum(res1[i-1][:j+1])
    return res1[k-1][n-1]
T=int(sys.stdin.readline())
n=[]
k=[]
res=[]
for i in range(T):
    k.append(int(sys.stdin.readline()))
    n.append(int(sys.stdin.readline()))
    res.append(apart(k[i],n[i]))
for i in res:
    print(i)

    



