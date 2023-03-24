def divisor(res, lst : list): # 약수를 구해주는 함수
    for i in range(1,int(res**0.5)+1):
        if res % i == 0:
            lst.append(i)
            lst.append(res//i)
    return lst

# x는 분자, y는 분모 x/y
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
res1,res2 = x1*y2 + x2*y1, y1*y2 

# 두 수가 서로소가 될때까지 나눔
lst1,lst2=[],[]
lst1,lst2 = divisor(res1, lst1), divisor(res2,lst2)
t = max(set(lst1) & set(lst2))

print(res1//t,res2//t)
