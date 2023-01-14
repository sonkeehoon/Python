def solution(land):
    # 다른 사람의 코드에서 힌트를 얻었습니다.
    answer = 0
    for i in range(1,len(land)):
        land[i][0] += max(land[i-1][1],land[i-1][2],land[i-1][3])
        land[i][1] += max(land[i-1][0],land[i-1][2],land[i-1][3])
        land[i][2] += max(land[i-1][1],land[i-1][0],land[i-1][3])
        land[i][3] += max(land[i-1][1],land[i-1][2],land[i-1][0])
    answer = max(land[-1])

    return answer