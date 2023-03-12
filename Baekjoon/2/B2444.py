import sys
input= sys.stdin.readline

N= int(input())
# 나의 코드..
# k = 2*N-1
# for i in range(k):
#     for j in range(k):
#         if i <= N-1:
#             if j-i > N-1:
#                 continue
#         else:
#             if i+j > 3*(N-1):
#                 continue
#         if N-1<= i+j<= 3*(N-1) and abs(i-j)<=N-1:
#             print("*",end='')
#         elif abs(i-j)>N-1 and i+j> 3*(N-1):
#             continue
#         else: print(" ",end='')
#     print()

# 간단한 코드(다른사람의 정답코드)
for i in range(N):
    print(' '*(N-1-i)+'*'*(2*i+1))
for j in range(N-2,-1,-1):
    print(' '*(N-1-j)+'*'*(2*j+1))