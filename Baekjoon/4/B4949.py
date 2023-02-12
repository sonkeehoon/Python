import sys
input = sys.stdin.readline
while True:
    tmp = []
    stack = []
    s = input().rstrip()
    # print(s)
    if s == '.':
        break
    for c in s:
        if c in '()[]':
            stack.append(c)
    while stack:
        if stack[-1] == "(" or stack[-1] == "[":
            if len(tmp) == 0:
                break
            x = stack[-1] + tmp[-1]
            if x == "()" or x == "[]":
                tmp.pop()
                stack.pop()
                continue
        
        p = stack.pop()       
        tmp.append(p)
    if len(stack) == len(tmp) == 0:
        print("yes")
    else:
        print("no")
        
               
    
    
    
    