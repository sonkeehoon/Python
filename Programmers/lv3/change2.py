# https://school.programmers.co.kr/learn/courses/30/lessons/12907
# 혼자 풀었는데 change1.py가 됐다.
# 질문 게시판을 참고해서 dp가 가능하다는 것을 알았고 이렇게 짰다
N = 1000000007
def solution(n, money):
    answer = 0
    dp = [0]*(n+1)
    dp[0] = 1
    for m in money: # m = 1,2,5
        
        for i in range(m, n+1):
            dp[i] += dp[i-m]  
        
    return dp[-1]%N
print(solution(5,[1,2,5]))