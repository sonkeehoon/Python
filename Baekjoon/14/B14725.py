import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) # 먹이의 정보 개수
K=[]
depth = "--"
tmp = []
for _ in range(N): # 로봇 개미 한마리가 보내준 정보
    K.append(input().split())
    tmp.append(K[-1][0])
min_len = int(min(tmp))
K.sort(key = lambda x:x[1:min_len+1])
for i in range(1,len(K[0])):
    print(depth*(i-1)+K[0][i])
for i in range(1, N):
    size = len(K[i])
    for j in range(1,size):
        if j >= len(K[i-1]):
            print(depth*(j-1) + K[i][j])
            continue
        if K[i][j] != K[i-1][j]:
            print(depth*(j-1) + K[i][j])
        
    
