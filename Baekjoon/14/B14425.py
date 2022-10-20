import sys
input=sys.stdin.readline
N,M=map(int,input().split())
S=[]
for i in range(N):
    S.append(input().rstrip())
cnt=0
for i in range(M):
    x=input().rstrip()
    if x in S:
        cnt+=1
print(cnt)