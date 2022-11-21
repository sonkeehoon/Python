cards1=[[13, 21, 24, 29, 50], [1, 12, 20, 21, 32], [16, 26, 34, 46, 52], [9, 11, 16, 16, 21], [3, 8, 10, 16, 20]]
cards2=[[5, 10, 15, 41, 49], [6, 14, 15, 19, 46], [5, 42, 43, 51, 52], [5, 6, 11, 13, 45], [5, 9, 11, 13, 45]]
res=0
for i in range(len(cards1)):
    if len(set(cards1[i]+cards2[i]))!=10:
        res+=1
        continue
    else:
        if i==0:
            continue
        if len(set(cards1[i-1]+cards1[i]))<9 or len(set(cards2[i-1]+cards2[i]))<9:
            res+=1
print(res)
    