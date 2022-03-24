def H_num(N):
    count=99
    if N<100:
        return N
    for i in range(100,N+1):
        s=str(i)
        if i==1000:
            return count
        elif int(s[-1])-int(s[-2])==int(s[-2])-int(s[-3]):
            count+=1
    return count

N=int(input())

print(H_num(N))
