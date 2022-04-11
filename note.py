# isum=0
# for i in range(3333,10000,1):
#     if i%1234==0:
#         print(i)
#         isum+=i
#         if isum>=100000:
#             break
#         else:
#             continue
# print(isum)

# 2차원 리스트를 초기화 할때 꼭 이런방식으로 하자
k,n=3,3
res1=[]
for i in range(k):
    line=[]
    for j in range(n):
        line.append(0)
    res1.append(line)
print(res1)

        