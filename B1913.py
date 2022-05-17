import sys
input=sys.stdin.readline
n=int(input().rstrip())
a=list(map(int,input().split()))
sub=[0]*n
sub[0]=a[0]
for i in range(1,n):
    sub[i]=max((sub[i-1]+a[i]),a[i]) # 연속 부분합을 dp로 구현
print(max(sub))

