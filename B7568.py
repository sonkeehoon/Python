N=int(input())
w,h=[],[]
for i in range(N):
    x,y=map(int,input().split())
    w.append(x)
    h.append(y)
rank=[1]*N
for i in range(N):
    for j in range(N):
        if w[i]<w[j] and h[i]<h[j]:
            rank[i]+=1
    print(rank[i],end=' ')
# for i in rank:
#     print(i,end=" ")