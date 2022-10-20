import sys
input=sys.stdin.readline
N=int(input())
for i in range(N):
    num=int(input())
    clot,lst,d=[],[],{}
    cnt=1
    for j in range(num):
        lst.append(input().rstrip())
    for j in range(len(lst)):
        clot.append(lst[j].split())
        if clot[j][1] in d:
            d[clot[j][1]].append(clot[j][0])
            continue
        d[clot[j][1]]=[clot[j][0]]
    for j in d.values():
        cnt*=len(j)+1
    print(cnt-1)