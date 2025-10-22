# 오큰수: https://www.acmicpc.net/problem/17298
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = []  # 오큰수를 찾기 위해 사용할 스택
res = [-1] * N  # 정답 배열

for i in range(N - 1, -1, -1):  # 뒤에서부터 순회
    
    # 스택에서 A[i]보다 작거나 같은 값들은 제거
    while stack and stack[-1] <= A[i]:
        stack.pop()
    
    # 스택이 비지 않았다면, 그 맨 위가 오큰수
    if stack:
        res[i] = stack[-1]
    
    # 현재 값을 스택에 추가
    stack.append(A[i])

print(*res)
