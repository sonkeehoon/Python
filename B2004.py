import sys
def div(x,y):
    cnt=0
    while y<=x:
        x=x//y
        cnt+=x
    return cnt
input=sys.stdin.readline
n,m=map(int,input().split())
x1,y1=div(n,2),div(n,5)
x2,y2=div(n-m,2),div(n-m,5)
x3,y3=div(m,2),div(m,5)
print(min(x1-x2-x3,y1-y2-y3))