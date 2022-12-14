# 68.8
import math
def solution(k, d):
    answer = 0
    
    n = d//k
    
    for i in range(n+1):
        answer += int(math.sqrt(d**2-(i*k)**2))//k + 1
    
    
    
      
    return answer

print(solution(2,4))