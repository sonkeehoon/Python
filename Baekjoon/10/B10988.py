# W = input()
# i = 0
# size = len(W)
# # print(size)
# while i < size//2:
#     if W[i] == W[size-(i+1)]:
#         i += 1
#         continue
#     print(0)
#     exit()
# print(1)

# 또 다른 아이디어
# W = input()
# reversed_W = W[::-1]
# if W == reversed_W:
#     print(1)
# else: 
#     print(0)

# 가장 낮은 40ms로 통과
W = input()
if W == W[::-1]: print(1)
else: print(0)