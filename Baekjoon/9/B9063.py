import sys
input = sys.stdin.readline

N = int(input())
dots = []

for _ in range(N):
    x,y = map(int,input().split())
    dots.append([x,y])

tmp = list(zip(*dots))

area = ((max(tmp[0]) - min(tmp[0]))*(max(tmp[1]) - min(tmp[1])))
print(area)