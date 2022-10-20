from math import factorial as fact
N=int(input())
fact_lst=list(map(lambda x: int(x),list(str(fact(N)))))
fact_len=len(str(fact(N)))
cnt=0
for i in range(fact_len-1,-1,-1):
    if fact_lst[i]==0:
        cnt+=1
        continue
    break
print(cnt)