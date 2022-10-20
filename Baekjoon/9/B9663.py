import sys
input=sys.stdin.readline
N = int(input())
queen = [0] * N
res = 0
def check(x):
    for i in range(x):
        # 같은열,같은행에 퀸이 있거나 or 대각선에 퀸이 존재하면:
        # dfs(x+1)를 호출하지 않음
        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == x - i:
            return False
    return True

def dfs(x):
    global res

    if x == N:
        res += 1
    else:
        for i in range(N):
            queen[x] = i
            # 새로놓은 퀸의 같은열,같은행,대각선에 퀸이 있는지 check
            # 겹치는 퀸이 있으면 오른쪽으로 한칸 옮긴다.
            if check(x):
                dfs(x+1) # 없으면 통과! 그 다음줄로

dfs(0)
print(res)
# 혼자서는 도저히 풀리지가 않아서 한 블로그의 코드를 먼저 보고 이해했습니다.
# 스스로 짠 코드는 결코 아님을 알려드립니다.
# https://blog.naver.com/mkdusgml/222539686023