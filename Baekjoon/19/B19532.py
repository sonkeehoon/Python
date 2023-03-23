a,b,c,d,e,f = map(int,input().split())

# 브루트 포스 풀이
# start, end = -999,999
# for x in range(start, end+1):
#     for y in range(start, end+1):
#         if a*x+b*y == c and d*x + e*y == f:
#             print(x,y)
#             exit()
    
# 더 효율적이고 수학적인 풀이
# 2원 1차 연립방정식의 해는 공식이 있다
# ax+by=c, dx+ey=f 의 경우 
# x = (c*e-b*f)//(a*e-b*d)
# y = (c*d-a*f)//(b*d-a*e)
x = (c*e-b*f)//(a*e-b*d)
y = (c*d-a*f)//(b*d-a*e)
print(x,y)
