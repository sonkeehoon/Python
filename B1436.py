N=int(input())
lst=[]
i=0
while len(lst)!=N:
    if '666' in str(i):
        lst.append(i)
    i+=1
print(sorted(lst)[N-1])