N = int(input())
lst = [[0 for _ in range(10)] for _ in range(N+1)]
lst[1] = [0,1,1,1,1,1,1,1,1,1]
for i in range(2,N+1):
    lst[i][0] = lst[i-1][1]
    lst[i][9] = lst[i-1][8]
    for j in range(1,9):
        lst[i][j] = lst[i-1][j-1] + lst[i-1][j+1]
print(sum(lst[-1])%10**9)
