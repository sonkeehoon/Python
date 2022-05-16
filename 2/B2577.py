from operator import countOf

a=int(input())
b=int(input())    
c=int(input())
res=str(a*b*c)
for i in range(10):
    print(countOf(res,"{}".format(i)))