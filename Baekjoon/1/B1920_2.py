# 수 찾기 : https://www.acmicpc.net/problem/1920
N = input()
A = set(map(int,input().split()))
M = input()
lst = list(map(int,input().split()))

for num in lst:
    if num in A:
        print(1)
        continue
    print(0)
