import sys
input=sys.stdin.readline
N=int(input())
card = list(map(int, input().split()))
M=int(input())
lst = list(map(int, input().split()))
cnt = {}
for c in card:
    if c in cnt:
        cnt[c] += 1
    else:
        cnt[c] = 1
print(cnt)
print(' '.join(str(cnt[key]) if key in cnt else '0' for key in lst))