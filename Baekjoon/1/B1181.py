N=int(input())
lst=[]
len_lst=[]
sorted_lst=[]
for i in range(N):
    lst.append(input())
    len_lst.append(len(lst[-1]))
lst=sorted(list(set(lst)))
for i in range(1,max(len_lst)+1):
    for j in range(len(lst)):
        same_len_lst=[]
        if len(lst[j])==i:
            same_len_lst.append(lst[j])
        else: continue
        same_len_lst.sort()
        sorted_lst.append(same_len_lst)
for i in range(len(sorted_lst)):
    print(sorted_lst[i][0])