# 베르트랑 공준은 에라토스 테네스의 체를 활용해서 시간을 줄이자!
import sys
def Prime(N):
    last=int(N**0.5) 
    for i in range(2,last+1):
        if N%i==0:
            return False
    return True
lst=[]
for i in range(2,246912):
    if Prime(i):
        lst.append(i)
while True:
    M=int(sys.stdin.readline())
    cnt=0
    if M==0: break
    for i in lst:
        if M<i<=2*M:
            cnt+=1
    print(cnt)