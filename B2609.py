M,N=map(int,input().split())
max_lst=[]
for i in range(1,min(M,N)+1):
    if M%i==0 and N%i==0:
        max_lst.append(i)
div=max(max_lst)
print(div,M*N//div,sep='\n')