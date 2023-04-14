# 주유소 : https://www.acmicpc.net/problem/13305
# 스스로 해결 여부 : O (but 장시간 소요)
# 시간을 재보지는 않았는데 체감상 1시간 반 정도 걸린 것 같다
import sys
input = sys.stdin.readline

N = int(input()) # 도시의 개수
dist = list(map(int,input().split())) # 각 도로의 길이
prices = list(map(int,input().split())) # 주유소의 리터당 가격(원)
# dist[i]는 도시i와 도시i+1간의 거리

total,i = 0,0
min_price = min(prices)
while prices[i] != min_price:
    now, nxt = prices[i], prices[i+1]
    if now >= nxt:
        total += now*dist[i]
        i += 1
    elif now < nxt:
        for j in range(1, N-i):
            if now > prices[i+j]: # 그다음 작은비용이 최초로 나오면
                total += sum(dist[i:i+j])*now
                i += j
                break
            
print(total+sum(dist[i:])*min_price)
                
                
                
            
