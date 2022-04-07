N=int(input())
i=0
while True:
    if N==1:
        print(1)
        break
    elif N<3*i*i-3*i+2:
        print(i)
        break
    i+=1