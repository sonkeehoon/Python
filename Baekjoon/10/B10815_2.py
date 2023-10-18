N = input()
cards = set(map(int,input().split()))
M = int(input())
lst = list(map(int,input().split()))

res = [0]*M
for i,v in enumerate(lst):
    if v in cards:
        res[i] = 1

print(*res)