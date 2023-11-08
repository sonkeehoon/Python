# 수 찾기 : https://www.acmicpc.net/problem/1920
import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=list(map(int,input().split()))
A=set(A)
for i in B:
    if i in A:
        print(1)
        continue
    print(0)