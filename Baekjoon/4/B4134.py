def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0 :
            return False
    return True
    
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    if n < 2:
        print(2)
        continue
    
    i = 0
    while not is_prime(n+i):
        i += 1
    print(n+i)
        