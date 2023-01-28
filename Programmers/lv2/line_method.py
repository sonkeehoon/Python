# https://school.programmers.co.kr/learn/courses/30/lessons/12936 : 줄 서는 방법
# 이상하게 시간을 많이 잡아먹은 문제.. 질문하기를 보면서 풀었다
# solution2는 시간초과가 난다. solution1으로 풀면 효율성 테스트까지 통과.
def solution1(n, k): # TC : n = 4, k = 22, result = [4,2,3,1]
    answer = [0]*n
    people = [i+1 for i in range(n)]
    factorial = [1,1]
    for i in range(2, n):
        factorial.append(i*factorial[i-1])
    factorial = list(reversed(factorial))
    k -= 1
    for i in range(n):
        answer[i] =  people[k//factorial[i]]
        people.remove(answer[i])
        k = k % factorial[i]
    return answer
print(solution1(4,24))

from itertools import permutations as perm
def solution2(n,k):
    lst = [i+1 for i in range(n)]
    answer = list(perm(lst,n))[k-1]
    return list(answer)
print(solution2(4,24))
    