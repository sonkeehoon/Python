import sys,copy
input=sys.stdin.readline
S=input().rstrip()
q=int(input())
lst=[[0]*26 for _ in range(len(S)+1)]
for i in range(1,len(S)+1):
    lst[i]=lst[i-1].copy()
    lst[i][ord(S[i-1])-97]+=1
for i in range(q):
    t=list(map(str,input().split()))
    t[1:]=map(lambda x: int(x), t[1:])
    print(lst[t[2]][ord(t[0])-97]-lst[t[1]][ord(t[0])-97])
# 각각 글자마다 26개(알파벳개수)짜리 리스트에 알파벳 빈도수를 저장(부분합)
# 혼자서 풀었을때는 50점이 한계였다.. 100점짜리는 남의 소스를 참고했다.
# 출처 : https://blog.naver.com/dhkimxx/222704333786