from itertools import combinations
N,M=map(int,input().split())
l=list(map(int,input().split()))
cl=list(combinations(l,3))
sumlist=[]
for i in range(len(cl)):
    if sum(cl[i])<=M:
        sumlist.append(sum(cl[i]))
sumlist=set(sumlist)
print(max(sumlist))
