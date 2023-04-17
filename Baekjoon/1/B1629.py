# 곱셈 : https://www.acmicpc.net/problem/1629
# 스스로 해결 여부 : O (pow 함수로만)
# pow 함수로 답만내고 넘어갔던 문제
import sys
input=sys.stdin.readline
A,B,C=map(int,input().split())
# print(pow(A,B,C)) 꼼수(?)로 썼던 함수

# 예전에 꼼수로 풀고 넘어갔었다. 원래는 분할정복으로 풀어야한다
# B11444번 문제에서 분할정복을 마주쳤는데 기억이 안나서 이 문제(B1629.py)를 먼저 풀어보려고 한다
# https://www.acmicpc.net/problem/11444

def multi(a,b): # 재귀함수
    
    if b == 1:
        return a%C
    else:
        tmp = multi(a,b//2) # 쉽게 생각하면 반으로 계~속 쪼개고 홀수인지 짝수인지에 따라 분기를 나눠준다
        if b % 2 == 0: # 짝수면
            return (tmp**2)%C
        else:
            return ((tmp**2)*a)%C

print(multi(A,B))