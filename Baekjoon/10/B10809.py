from operator import indexOf
S=input()
lst=[0]*26
for i in range(len(S)):
    for j in range(ord('a'),ord('z')+1):
        if chr(j) in S:
            lst[j-97]=indexOf(S,chr(j))
        else:
            lst[j-97]=-1
for i in range(len(lst)):
    print(lst[i],end=' ')