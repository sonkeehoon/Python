# 알고리즘 수업 - 칸토어 집합 : https://www.acmicpc.net/problem/4779
# 스스로 해결 여부 : X
# 혼자 짰는데 마지막에 '파일의 끝에서 입력을 멈춘다' 처리하는 부분은 검색해서 찾아봤다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def cantor(s):
    size = len(s)
    if s == ["-"]:
        return s
    part = size//3
    s[part:part*2] = [" "]*part
    s[:part] = cantor(s[:part])
    s[part*2:] = cantor(s[part*2:])
    return s   

while 1:
    try:
        N = int(input())
        s = list("-"*(3**N))
        print(''.join(cantor(s)))
    except:
        break