# 숫자를 입력받으면 그 다음(입력값 보다 크거나 같은 소수중 가장 작은) 소수를 출력하는 코드
# https://www.acmicpc.net/problem/4134
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
        