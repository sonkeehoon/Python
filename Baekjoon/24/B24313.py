# 알고리즘 수업 - 점근적 표기 1 : https://www.acmicpc.net/problem/24313
# 스스로 해결 여부 : O
# 혼자풀긴 했는데 질문게시판의 반례들을 참고했다

# from math import ceil
# a, b = map(int,input().split())
# c = int(input())
# n = int(input())

# if a < c:
#     if ceil(b/(c-a)) <= n: print(1)
#     else: print(0)
    
# elif a == c:
#     if b <= 0: print(1)
#     else: print(0)
    
# else: print(0)

a,b=map(int,input().split())
c=int(input())
d=int(input())
if a*d+b<=c*d and a<=c :
    print(1)
else:
    print(0)
