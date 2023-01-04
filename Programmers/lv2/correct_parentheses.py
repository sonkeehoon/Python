# 올바른 괄호 : https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    l = len(s)
    if l % 2 == 1 or s[-1] == '(' or s[0] == ')' or len(s) != 2*s.count('(') :
        return False
    
    for i in range(1,l):
        if s[i-1] == '(' and s[i] == ')' :
            s = 'x'*2 + s[:i-1] + s[i+1:]
    if s == 'x'*l:
        return True
    return False

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()()"))