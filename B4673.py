def d(n):
    if n<10:
        return 2*n
    else:
        sum=0
        for j in range(1,len(str(n))+1):
            sum+=int(str(n)[-j])
        
        return n+sum
  
a=[N for N in range(1,10001)]
res=[]

for i in range(10000):
    num=d(a[i])
    if num in a:
        res.append(num)
for k in range(len(res)):
    try:
        a.remove(res[k])
    except ValueError:
        pass
for _ in range(len(a)):
    print(a[_])  