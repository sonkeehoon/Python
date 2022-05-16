A,B=input().split(" ")
a=""
b=""
for i in range(3):
    a+=A[2-i]
    b+=B[2-i]
if a>b: print(a)
else : print(b)
