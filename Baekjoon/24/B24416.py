import sys
input = sys.stdin.readline

def fibonacci(n):
    global cnt
    f = [0,1,1]
    for i in range(3, n+1):
        cnt += 1
        f.append(f[i-1] + f[i-2])
    
    return f[n]

n = int(input())
cnt = 0
print(fibonacci(n),cnt)

