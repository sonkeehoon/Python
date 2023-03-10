import sys
input= sys.stdin.readline

N= int(input())
k = 2*N-1
for i in range(k):
    for j in range(k):
        if i <= N-1:
            if j-i > N-1:
                continue
        else:
            if i+j > 3*(N-1):
                continue
        if N-1<= i+j<= 3*(N-1) and abs(i-j)<=N-1:
            print("*",end='')
        elif abs(i-j)>N-1 and i+j> 3*(N-1):
            continue
        else: print(" ",end='')
    print()
