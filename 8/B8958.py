def score(s):
    res=0
    count=0
    for k in range(len(s)):
        if s[k]=="O":
            count+=1
            res+=count
        else:
            count=0
            continue
    return res
            
N=int(input())
lst=[0]*N
s=[0]*N
for i in range(N):
    lst[i]=input()
    s[i]=score(lst[i])
for j in range(N):
    print(s[j])