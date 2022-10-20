from operator import indexOf
w=input()
uw=w.upper()
lst=list(set(uw))
cnt=[0]*len(lst)
for i in range(len(lst)):
    cnt[i]=uw.count(lst[i])
if cnt.count(max(cnt))>1:
    print("?")
else:
    index=indexOf(cnt,max(cnt))
    print(lst[index])