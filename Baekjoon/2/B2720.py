import sys
input = sys.stdin.readline

coins = [25, 10, 5, 1]
T = int(input())
for _ in range(T):
    C = int(input())
    res = []
    
    for coin in coins:
        res.append(C//coin)
        C = C % coin
    print(*res)
    