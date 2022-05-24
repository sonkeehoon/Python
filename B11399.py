N=int(input())
P=list(map(int,input().split()))
d={}
for i in range(len(P)):
    d[P[i]]=[]
for i in range(len(P)):
    d[P[i]].append(i+1)
d=sorted(d.items())
lst,s_lst=[],[]
for i in range(len(d)):
    s=len(d[i][1])
    for j in range(s):
        lst.append(d[i][0])
for i in range(len(lst)):
    s_lst.append(sum(lst[:i+1]))
print(sum(s_lst))