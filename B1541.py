A=input()
idx,lst=[0],[]
for i in range(len(A)):
    if A[i]=='+' or A[i]=='-':
        idx.append(i)
if '-' not in A and '+' not in A:
    print(int(A))
    exit()
    
lst.append(A[:idx[1]])
lst.append(A[idx[1]])
idx.append(len(A))
for i in range(1,len(idx)-1):
    lst.append(A[idx[i]+1:idx[i+1]])
    if i==len(idx)-2:
        break
    lst.append(A[idx[i+1]])
res=int(lst[0])
for i in range(len(lst)):
    if i%2==0:
        lst[i]=int(lst[i])
for i in range(lst.count('+')):
    lst.remove('+')
if '-' not in lst:
    print(sum(lst))
    exit()
lst.append('-')
idx=[]
# print(lst)
for i in range(len(lst)):
    if lst[i]=='-':
        idx.append(i)
# print(idx)
res=sum(lst[:idx[0]])
for i in range(len(idx)-1):
    res-=sum(lst[idx[i]+1:idx[i+1]])
print(res)
    
        
    