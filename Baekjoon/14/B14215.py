a,b,c = sorted(map(int,input().split()))
if a + b <= c:
    print(a+b+(a+b-1))
else: print(a+b+c)
