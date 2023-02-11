# https://school.programmers.co.kr/learn/courses/30/lessons/12907
# 35점을 받은 풀이(시간초과)
# change2.py는 dp로 통과한 풀이
from itertools import product
N = 1000000007
def solution(n : int, money : list):
    answer = 0
    lst = []
    for m in money:
        end = n//m
        lst.append([i for i in range(end+1)])
    for case in product(*lst):
        sum = 0
        for i,j in zip(case,money):
            sum += i*j
            
        if sum == n:
            answer += 1
        elif sum > n:
            continue
        
    return answer%N

print(solution(5,[1,2,5]))