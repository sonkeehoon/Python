N,K = map(int,input().split())

lst = []
for i in range(1, int(N**0.5)+1):
   if N%i == 0: 
       lst.append(i)
       lst.append(N//i)
lst = list(set(lst))
lst.sort()
if len(lst) < K: print(0)
else: print(lst[K-1])
    