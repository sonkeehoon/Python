# 팩토리얼 2 : https://www.acmicpc.net/problem/27433
# 스스로 해결 여부 : O

def fib(N):
    if N == 1 or N == 0:
        return 1
    return N*fib(N-1)
print(fib(int(input())))