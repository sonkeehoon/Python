# 괄호의 값: https://www.acmicpc.net/problem/2504
from collections import deque
import sys
input = sys.stdin.readline
lst = list(input().strip())

flag = True
if len(lst) % 2 == 1:
    flag = False

q = deque()


while lst and flag:
    print(lst, q)
    tmp = lst.pop()
    
    if tmp in (')', ']'):
        q.append(tmp)
        
    elif tmp == '[':
        
        if q and q[-1] not in (')', '('):
            if q[-1] == ']':
                q.pop()
                q.append(3)
                
            elif type(q[-1]) == int:
                val = 0
                
                while q and type(q[-1]) == int:
                    val += q.pop()
                
                if q and q[-1] == ']':
                    q.pop()
                    q.append(3 * val)
                else:
                    flag = False
                    break        
    
        else:
            flag = False
            break
        
    elif tmp == '(':
        
        if q and q[-1] not in ('[', ']'):
            if q[-1] == ')':
                q.pop()
                q.append(2)
            
            elif type(q[-1]) == int:
                val = 0
                
                while q and type(q[-1]) == int:
                    val += q.pop()
                    
                if q and q[-1] == ')':
                    q.pop()
                    q.append(2 * val)
                
                else:
                    flag = False
                    break  
                
        else:
            flag = False
            break

if ']' in q or ')' in q:
    flag = False
print(sum(q) if flag else 0)
