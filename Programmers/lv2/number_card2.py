# 숫자 카드 나누기 : https://school.programmers.co.kr/learn/courses/30/lessons/135807
# 첫 시도 : 72.2 / 100.0 (number_card1.py)
# 두번째 시도 : https://blog.naver.com/jasuil/222932284293 에서 힌트를 얻고 100.0 / 100.0

import math 
    
def solution(arrayA, arrayB):
    result = []
    answer = 0
    arrayA = list(set(arrayA))
    arrayB = list(set(arrayB))
    
    a_div, b_div = arrayA[0], arrayB[0] # 각 리스트의 최대공약수를 담을 a_div, b_div
    for A in arrayA:
        a_div = math.gcd(a_div, A)
    for B in arrayB:
        b_div = math.gcd(b_div, B)
    
    for B in arrayB: # arrayB의 원소들이 a_div로 나누어 떨어 지는지 판별
        if B%a_div != 0 :
            if B == arrayB[-1]:
                result.append(a_div)
            continue
        break
    
    for A in arrayA: # arrayA의 원소들이 b_div로 나누어 떨어 지는지 판별
        if A%b_div != 0 :
            if A == arrayA[-1]:
                result.append(b_div)
            continue
        break
            

    if result == []:
        return 0
    answer = max(result)
    return answer



print(solution([10, 17], [5, 20]))
print(solution([10, 20], [5, 17]))
print(solution([14, 35, 119], [18, 30 ,102]))
print(solution([3], [100]))
