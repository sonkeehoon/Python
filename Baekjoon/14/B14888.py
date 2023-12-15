# 연산자 끠워넣기 : https://www.acmicpc.net/problem/14888
import sys
from itertools import permutations as perm

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split())) # 숫자
operator_cnt = list(map(int, input().split())) # 연산 (+, -, *, //)
operator = ['+','-','*','//']
operator2 = []

for i in range(4):
    for _ in range(operator_cnt[i]):
        operator2.append(operator[i])
        
def calc(x, y, case):
    if case == '+': return x + y
    elif case == '-': return x - y
    elif case == '*': return x * y
    elif case == '//': 
        if x < 0:
            return - (abs(x) // y)
        else:
            return x//y

minnum = int(1e10)
maxnum = -int(1e10)
cases = set(perm(operator2, N-1)) # set이 아닌 list로 하면 중복인 케이스까지 넣어서 시간초과

for case in cases:
    total = calc(A[0], A[1], case[0])
    
    for i in range(1, N-1):
        total = calc(total, A[i+1], case[i])
        
    maxnum = max(maxnum, total)
    minnum = min(minnum, total)

print(maxnum)
print(minnum)
