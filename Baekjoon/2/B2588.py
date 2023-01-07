# with 준영
a = int(input())
b = int(input())

sum = 0
for idx,n in enumerate(reversed(str(b))):
    num = int(n)
    res = num * a
    print(res)
    sum += res * (10**idx)
    
print(sum)

    