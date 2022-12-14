# 점 찍기 : https://school.programmers.co.kr/learn/courses/30/lessons/140107
# 쉬울줄 알았는데 생각보다 어려웠다.. 처음엔 68.8을 받았고
# 다른사람의 코드를 참고했다..
import math
def solution(k, d):
    answer = 0
    n = d//k
    for i in range(n+1):
        answer += int(math.sqrt(d**2-(i*k)**2))//k + 1
    
    return answer

print(solution(2,4))
