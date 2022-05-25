import sys
input=sys.stdin.readline
N,K=map(int,input().split())
res=[[0 for _ in range(K+1)][:] for _ in range(N+1)]
# res=[0]*(K+1) 이렇게 풀지말고 2차원 리스트로 풀자
# for i in range(N):
#     W,V=map(int,input().split())
#     b[W]=V
# 물건을 리스트에 담지 말고 하나씩 넣으면서 2차원 리스트를 완성시키자
# 즉,K=7일때
# w1,v1=6,13 에서 한줄 완성
# w2,v2=4,8 에서 다음줄 완성
# 이런순서로 wN,vN 줄 까지 완성
# 이러한 문제를 knapsack(냅색)문제 라고한다
# 혼자서 짠 코드는 시간초과가 떴다. 그래서 다른사람의 코드를 참고했다.
# 스스로 못풀었다고 너무 기죽지 말자..!
# 코드출처 : https://www.acmicpc.net/board/view/79619
for i in range(1,N+1):
    w,v=map(int,input().split())
    for j in range(1,K+1):
        if w>j:
            res[i][j]=res[i-1][j]
            continue
        res[i][j]=max(res[i-1][j],res[i-1][j-w]+v)
print(res[N][K])