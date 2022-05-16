import sys
input=sys.stdin.readline
T=int(input())
zero,one=[],[]
for i in range(41):
    if i==0:
        zero.append(1)
        one.append(0)
        continue
    elif i==1:
        zero.append(0)
        one.append(1)
        continue
    else:
        zero.append(zero[i-1]+zero[i-2])
        one.append(one[i-1]+one[i-2])
for i in range(T):
    x=int(input())
    print(zero[x],one[x])