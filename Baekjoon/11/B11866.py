import sys
input = sys.stdin.readline
N,K = map(int,input().split())
q =[i+1 for i in range(N)]
i = 0
res = []
for _ in range(N):
    i += K-1
    l = len(q)
    if i < l:
        res.append(q.pop(i))
        continue
    while i >= l:
        i -= l
    res.append(q.pop(i))
print("<",end='')
print(*res,sep=', ',end='')
print(">")
    