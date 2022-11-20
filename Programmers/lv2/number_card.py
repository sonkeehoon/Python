# 숫자 카드 나누기 : https://school.programmers.co.kr/learn/courses/30/lessons/135807
# 72.2 / 100 (미완)
def allDivide(lst, div):
    for i in lst:
        if i%div != 0:
            return False
    return True

def notAllDivide(lst, div):
    for i in lst:
        if i%div == 0:
            return False
    return True 
    
    
def solution(arrayA, arrayB):
    result = []
    answer = 0
    num = max(min(arrayA), min(arrayB))
    
    for i in range(num, 0, -1):
        if (allDivide(arrayA, i) and notAllDivide(arrayB, i)) or (allDivide(arrayB, i) and notAllDivide(arrayA, i)):
            result.append(i)
            break
            
    if result == []:
        return 0
    answer = result[0]
    return answer



print(solution([10, 17], [5, 20]))
print(solution([10, 20], [5, 17]))
print(solution([14, 35, 119], [18, 30 ,102]))
print(solution([3], [100]))