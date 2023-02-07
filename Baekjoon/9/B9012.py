import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    stack = list(input().strip())
    tmp = []
    while stack:
        if stack[-1] == "(":
            if len(tmp) == 0:
                break
            tmp.pop()
            stack.pop()
            continue
        p = stack.pop()       
        tmp.append(p)
    if len(stack) == len(tmp) == 0:
        print("YES")
    else:
        print("NO")
        
    
            
            
        
        
        
    
    
    