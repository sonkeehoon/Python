import sys
input=sys.stdin.readline
N,K=map(int,input().split())
lst=[0]+list(map(int,input().split()))
for i in range(1,N+1):
    lst[i]=lst[i-1]+lst[i]
n=-10**9
for i in range(0,N-K+1):
    if n<lst[i+K]-lst[i]:
        n=lst[i+K]-lst[i] # 다음항의 온도의 합이 더 크면 n에 대입
# 크지 않으면 그냥 넘어간다.
# 시간을 줄이려면 for문 안에 sum을 사용하지 말자
print(n)