import sys
input=sys.stdin.readline
N,M=map(int,input().split())
A=[]
for i in range(N):
    a=list(map(int,input().split()))
    A.append(a)
M,K=map(int,input().split())
B=[]
for j in range(M):
    b=list(map(int,input().split()))
    B.append(b)
R=[]
for i in range(N):
    line=[]
    for j in range(K):
        line.append(0)
    R.append(line)
for i in range(N):
    for j in range(K):
        s=0
        for k in range(M):
            s+=A[i][k]*B[k][j]
        print(s,end=' ')
    print()