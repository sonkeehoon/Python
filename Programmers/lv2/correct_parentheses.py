# 올바른 괄호 : https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    from collections import deque
    s = deque(s)
    q = deque()
    while s:
        tmp = s.pop()
        q.appendleft(tmp)
        try:
            if q[0] == "(" and q[1] == ")":
                q.popleft()
                q.popleft()                
        except IndexError:
            break              
    if q:
        return False
    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()()"))