# 귤 고르기 : https://school.programmers.co.kr/learn/courses/30/lessons/138476
from collections import Counter
def solution(k, tangerine):
    answer = 0
    res = []
    tang_cnt = Counter(tangerine)
    # print(tang_cnt)
    tang_cnt = dict(sorted(tang_cnt.items(), key = lambda x : x[1], reverse = True)) # value기준 내림차순으로 정렬
    print(tang_cnt)
    # print(tang_cnt)
    for v in tang_cnt.values():
        if k - v <= 0:
            answer += 1
            return answer
        k -= v
        answer += 1
             
    return answer
        


print(solution(2,[1, 1, 1, 1, 2, 2, 2, 3]))