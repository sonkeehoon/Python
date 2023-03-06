import sys
input = sys.stdin.readline
while 1:
    try:
        print(input().rstrip())
    except EOFError:
        break
    
