# 2 x n 타일링 : https://school.programmers.co.kr/learn/courses/30/lessons/12900#

def solution(n):
    lst = [0,1,2]
    N = 1000000007
    for _ in range(n-2):
        lst.append((lst[-1] + lst[-2]) % N)
        
    return lst[n]