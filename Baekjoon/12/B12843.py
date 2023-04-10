# 복수전공 : https://www.acmicpc.net/problem/12843
# 스스로 해결 여부 : X
# 숭실대문제였고 제목에 끌려서 문제를 시도해봤다
# 분명 문제 내의 TC나 자체적으로 만들어본 TC도 맞게 출력이 되는데 틀렸다고 뜬다
# 질문게시판에 글도 별로 없고 해서 반례 찾기가 어려웠다..
# 그래서 일단 풀었다고 가정하고 넘어가려고 한다(채점 해보면 '틀렸습니다' 뜸)

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
d = {}
for _ in range(n):
    x,y = input().split()
    x = int(x)
    d[x] = (y,[])

for _ in range(m):
    x,y = map(int,input().split())
    d[x][1].append(y)
    d[y][1].append(x)
if m == 0:
    print(n)
    exit()
d = dict(sorted(d.items(), key = lambda x:len(x[1][1]), reverse = True))
lecture = list(d.keys())
cnt = 0
while lecture:
    tmp = lecture.pop()
    for i in d[tmp][1]:
        try:
            lecture.remove(i)
        except ValueError:
            pass
    cnt += 1 
print(cnt)


