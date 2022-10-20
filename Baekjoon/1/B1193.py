X=int(input())
i,k=0,1
lst=[0]
while True:
    if (i/2)*(i-1)+1<=X<=(i/2)*(i+1):
        k=i
        if i%2==0:
            lst[0]=[1,i]
            for j in range(1,i):
                lst.append([1+j,i-j])
            break
        elif i%2!=0:
            lst[0]=[i,1]
            for j in range(1,i):
                lst.append([i-j,j+1])
            break
    i+=1
idx=int(X-(k/2)*(k-1)-1)
print(str(lst[idx][0])+"/"+str(lst[idx][1]))