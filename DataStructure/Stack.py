import sys 
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    cmd = input().split()
    # print(cmd)
    cmd_name = cmd[0]
    stack_len = len(stack)
    
    if cmd_name == 'push':
        stack.append(cmd[1])
    elif cmd_name == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif cmd_name == 'size':
        print(stack_len)
    elif cmd_name == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif cmd_name == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])