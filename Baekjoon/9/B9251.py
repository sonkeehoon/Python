# https://suri78.tistory.com/11
# 위 글을 읽고 겨우 이해했다.. 나 혼자 이런생각은 못해낼것 같다
# 그냥 읽어보고 이런 알고리즘이 있구나 하고 넘어가려고 한다
import sys
input = sys.stdin.readline
A = input().strip()
B = input().strip()
A_len, B_len = len(A), len(B)
lst = [0]*B_len
# print(A,B,A_len,B_len)
for i in range(A_len):
    cnt = 0
    for j in range(B_len):
        if cnt < lst[j]:
            cnt = lst[j]
        elif A[i] == B[j]:
            lst[j] = cnt + 1

print(max(lst))
        
        
    

