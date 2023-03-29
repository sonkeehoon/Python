# 다른 사람 풀이를 참고했습니다
import sys
input = sys.stdin.readline
T = int(input())
n = []

for i in range(T):
    n.append(int(input()))
N = max(n)
# 에라토스 테네스의 체
Era = [True]*(N+1)
Era[0],Era[1] = False,False
for i in range(2,int(N**0.5)+1):
    if Era[i] == False: 
        continue
    for j in range(i+i, N+1, i):
        Era[j] = False

for i in n:
    cnt = 0
    if i == 2+2:
        cnt += 1
        print(cnt)
        continue
    for j in range(3, (i//2)+1,2):
        x,y = j, i-j
        if Era[x] and Era[y]:
            cnt += 1
    print(cnt)

            



                
        
    
    