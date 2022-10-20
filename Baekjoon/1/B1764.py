import sys
input=sys.stdin.readline
N,M=map(int,input().split())
ch,cs=set(),set()
for _ in range(N):
    ch.add(input().rstrip())
for _ in range(M):
    cs.add(input().rstrip())
res=list(ch&cs)
res.sort()
print(len(res))
for i in res:
    print(i)