# 우박수열 정적분 : https://school.programmers.co.kr/learn/courses/30/lessons/134239
# 첫시도 100.0 / 100.0

def solution(k, ranges):
    result = []
    seq = [k]
    area = []
    
    while True: # k 가 1이하가 될 때까지 반복
        if k>1 :
            if k%2 == 0:
                area.append((k+(k/2))/2)
                k = k/2
                seq.append(k)
                continue
            elif k%2 == 1:
                area.append((k+(3*k+1))/2)
                k = 3*k+1
                seq.append(k)
                continue        
        break
    
    for r in ranges: # x1 <= x <= x2 사이의 넓이 구하기
        x1 = r[0]
        x2 = len(seq)-abs(r[1])
        if x1 >= x2 : # 시작점이 끝점보다 큰 경우 -1
            result.append(-1)
            continue
        sum = 0
        for i in range(x1,x2-1):
            sum += area[i]
        result.append(sum)
    
    
    return result

solution(5,[[0,0],[0,-1],[2,-3],[3,-3]])
