import sys
T=int(sys.stdin.readline())
for _ in range(T):
    n=int(sys.stdin.readline())
    a = [False, False] + [True] * (n - 1)
    for i in range(2, int(n**0.5)+1):
        if a[i]:
            for j in range(2*i, n+1, i):
                a[j] = False
    for i in range(2,int(n/2)+1):
        if a[i] and a[n-i]:
            num1=i
            num2=n-i
    print(num1,num2)