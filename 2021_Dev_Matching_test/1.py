# 1. 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums): # win_nums = 당첨번호, lottos = 구매한 로또 번호
    
    zero = lottos.count(0) # lottos에서 0의 갯수
    lucky = len(set(lottos)&set(win_nums))  # 두 집합의 공통 원소를 lucky 리스트에 할당
    result = [7-(lucky+zero), 7-lucky] # 순위를 담은 result 리스트
    
    for i in range(len(result)): # 순위가 7 이상이면 전부 6으로 바꿔줌
        if result[i] >= 7:
            result[i] = 6
    
    return result

# print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))
