import time
def Prime(N):
    last=int(N**0.5) # 제곱근만 검사해도 소수인지 판별 가능
    for i in range(2,last+1):
        if N%i==0:
            return False
    return True
M,N=map(int,input().split())
start=time.time()
lst=[]
for i in range(M,N+1):
    if i==1:continue
    if Prime(i):
        lst.append(i)
# print("exe time is : {:.3f}".format(time.time()-start))
for j in lst:
    print(j)
print("exe time is : {:.3f}".format(time.time()-start)) 