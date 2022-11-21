balance=[100, 1, 1, 1, 1]
transaction=[[1, 2, 100], [2, 3, 101], [3, 4, 102], [4, 5, 103], [5, 1, 104]]
abnormal=[1]
balance=[0]+balance
for i in range(len(balance)):
    balance[i]=[0,balance[i]]
for trans in transaction:
    temp=[0,0]
    if balance[trans[0]][-1]>=trans[2]:
        balance[trans[0]][-1]-=trans[2]
        balance[trans[1]].append(trans[0])
        balance[trans[1]].append(trans[2])
        continue
    while balance[trans[0]][-1]<trans[2]:
        temp[1]=balance[trans[0]].pop()
        temp[0]=balance[trans[0]].pop()
        balance[trans[1]].append(temp[0])
        balance[trans[1]].append(temp[1])
        trans[2]-=temp[1]
        if balance[trans[0]][-1]>=trans[2]:
            balance[trans[0]][-1]-=trans[2]
            if balance[trans[0]][-2]==0:
                balance[trans[1]].append(trans[0])
                balance[trans[1]].append(trans[2])  
for ab in abnormal:
    balance[ab]=[0,0]
    for b in balance:
        if ab not in b:
            continue
        for j in range(0,len(b),2):
            if b[j]==ab:
                b[j+1]=0
for i in range(len(balance)):
    balance[i]=sum(balance[i][1::2])
balance.pop(0)
print(balance)
# 실패