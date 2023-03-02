import sys
input = sys.stdin.readline
N,M = map(int,input().split())
basket = [i+1 for i in range(N)]

for _ in range(M):
    i,j = map(int,input().split())
    # basket[i-1:j] = reversed(basket[i-1:j]) 
    basket[i-1:j] = basket[i-1:j][::-1] # reversed보다 [::-1] 이 속도가 약간더 빠름
    
print(*basket)