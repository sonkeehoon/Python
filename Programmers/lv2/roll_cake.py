# 롤케이크 자르기 : https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 다른사람의 코드를 참고했습니다.. Counter와 del 사용법에 감탄했다
# Counter로 전체 개수를 구한다음 pop으로 하나씩 빼고
# 뺀 원소를 set1에 집어넣고 비교

from collections import Counter
def solution(topping):
    # topping = [1, 2, 1, 3, 1, 4, 1, 2]
    answer = 0
    total = Counter(topping)
    set1 = set()
    while len(topping) > 1:
        element = topping.pop() # 2
        set1.add(element)
        if total[element] > 1:
            total[element] -= 1
        else:
            del total[element]
            
        if len(set1) == len(total):
            answer += 1        

    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))