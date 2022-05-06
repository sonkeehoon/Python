import sys
def P(N):
    if N<3:
        return 1
    lst=[1,1,1]
    for i in range(3,N):
        lst.append(lst[i-3]+lst[i-2])
    return lst[N-1]
input=sys.stdin.readline
T=int(input())
for i in range(T):
    print(P(int(input())))