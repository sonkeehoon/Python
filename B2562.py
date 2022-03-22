from operator import indexOf
lst=[0]*9

for i in range(9):
    lst[i]=int(input())

m=max(lst)
print(m,indexOf(lst,m)+1)