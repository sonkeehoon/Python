import sys
input=sys.stdin.readline
N=int(input())
cost=[]
for i in range(N):
    cost.append(list(map(int,input().split())))
min_cost=[]
min_cost.append(cost[0])
min_cost=[cost[0]]+[[0,0,0] for i in range(N-1)]
for i in range(1,N):
    min_cost[i][0]=min(min_cost[i-1][1],min_cost[i-1][2])+cost[i][0]
    min_cost[i][1]=min(min_cost[i-1][0],min_cost[i-1][2])+cost[i][1]
    min_cost[i][2]=min(min_cost[i-1][0],min_cost[i-1][1])+cost[i][2]
print(min(min_cost[N-1]))

