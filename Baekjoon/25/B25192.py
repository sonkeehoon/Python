# 인사성 밝은 곰곰이 : https://www.acmicpc.net/source/58594650
# 딕셔너리로 풀면 메모리 사용량을 더 줄일수 있나보다. 시간이 나면 시도해보자
import sys
input = sys.stdin.readline
s = set()
cnt = 0
for _ in range(int(input())):
    x = input()
    if x == "ENTER\n":
        cnt += len(s)
        s = set()
        continue
    elif x in s:
        continue
    s.add(x)
cnt += len(s)
print(cnt)
 