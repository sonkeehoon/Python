import sys
input = sys.stdin.readline
while 1:
    a,b,c = map(int,input().split())
    lengths = [a,b,c]
    lengths.sort()
    tmp = len(set(lengths))
    if a == b == c:
        if a == 0:
            break
        else:
            print("Equilateral")
            continue
    if lengths[2] >= lengths[0] + lengths[1]:
        print("Invalid")
    elif tmp == 2:
        print("Isosceles")
    elif tmp == 3:
        print("Scalene")
    else:
        print("Invalid")
        