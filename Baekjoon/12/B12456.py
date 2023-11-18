# 미 해결
import sys
input = sys.stdin.readline

T = int(input())
res = []
for idx in range(T):
    N, K = map(int,input().split())
    coffee = []    
    for _ in range(N):
        c, t, s = map(int,input().split())
        coffee.append([c,t,s])
    coffee.sort(key = lambda x:x[2], reverse = True)   
    i = 0
    ans = 0
    day = 0
    while day < K and i < N:
        if coffee[i][0] >= 1 and coffee[i][1] >= 1:        
            coffee[i][0] -= 1
            ans += coffee[i][2]
        for j in range(len(coffee)):
            coffee[j][1] -= 1
        if coffee[i][0] <= 0 or coffee[i][1] <= 0 :
            i += 1
        day += 1
    res.append(ans)
for idx, r in enumerate(res):
    print(f"Case #{idx+1}: {r}")