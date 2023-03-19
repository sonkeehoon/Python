A,B = map(int,input().split())
lst = []
for i in range(2, min(A,B)+1):
    if A%i == 0 and B%i == 0: # 공약수가 하나라도 존재하면
        lst.append(i)
        break
# print(lst)
if not lst: # 2이상의 공약수가 없으면 A*B 
        print(A*B)
else: # 있으면
    j = 2
    tmp = 1
    while j <= min(A,B):
        if A%j == 0 and B%j == 0:
            tmp *= j
            A,B = A//j,B//j
            j = 1
        j += 1
    print(tmp*A*B)
        
        
