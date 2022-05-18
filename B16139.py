import sys
input=sys.stdin.readline
S=input().rstrip()
q=int(input())
for i in range(q):
    lst=list(map(str,input().split()))
    lst[1:]=map(lambda x: int(x), lst[1:])