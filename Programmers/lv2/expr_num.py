# 숫자의 표현 : https://school.programmers.co.kr/learn/courses/30/lessons/12924
def solution(n):
    answer = 0
    lst = []
    if n == 1:
        return 1
    for div in range(1,int(n**0.5)+1):
        if n%div == 0:
            lst.append(div)
            lst.append(n//div)

    divisor = set(lst)
    for d in divisor:
        if d%2 == 1:
            answer += 1
    return answer

        