import sys
# from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
basket = [i+1 for i in range(N)]

# 나의 코드 
# for _ in range(M):
#     i,j,k = map(int,input().split())
#     queue = deque(basket[i-1:j])
#     while True:
#         queue.rotate(1)
#         if queue[0] == basket[k-1]:
#             break
#     basket[i-1:j] = list(queue)
# print(*basket)

# 더 간단한 방법 (다른 사람의 코드, 슬라이싱만으로 해결)
for _ in range(M):
    i,j,k = map(int,input().split())
    i,j,k = i-1,j-1,k-1
    basket = basket[:i] + basket[k:j+1] + basket[i:k] + basket[j+1:]
print(*basket)
