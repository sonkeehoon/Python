# 124 나라의 숫자 : https://school.programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ''
    lst = ['1', '2', '4']
    if 0 < n <= 3:
        return lst[n-1]
    while n > 0 :
        n -= 1
        answer += lst[n % 3]
        n //= 3
    return answer[::-1]

print(solution(15))