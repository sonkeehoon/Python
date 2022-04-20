import sys
while True:
    a=int(sys.stdin.readline())
    cnt=0
    if a==0:
        break
    elif a==1 or a==2:
        print(1)
        continue
    for j in range(a+1,(2*a)+1):
        for k in range(2,int(j**0.5)+1):
            if j%k==0:
                break
            elif k==int(j**0.5):
                cnt+=1
    print(cnt)