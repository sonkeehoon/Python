# 기사단원의 무기 : https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    import math
    answer = 0
    
    def yaksu(n):
        lst=[]
        for i in range(1,int(math.sqrt(n))+1):
            if n%i == 0:
                lst.append(i)
                if i**2 != n:
                    lst.append(n)
        return len(lst)
    
    num_lst = [yaksu(i+1) for i in range(number)]
    for n in num_lst:
        if n <= limit:
            answer += n
            continue
        answer += power
    
    return answer

print(solution(5,3,2))