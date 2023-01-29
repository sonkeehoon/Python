import sys
input = sys.stdin.readline
lst = []
for _ in range(5):
    lst.append(int(input()))
lst = sorted(lst)
print(sum(lst)//len(lst))
print(lst[2])