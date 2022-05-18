# 장시간 끝에 해결했는데 실버4였다니..
import sys
input=sys.stdin.readline
K=int(input())
d={1:[],2:[],3:[],4:[]}
lst=[]
for i in range(6):
    x,y=map(int,input().split())
    d[x].append(y)
    lst.append(y)
res=lst+lst
max_len,min_len=[],[]
for i in range(1,5):
    if len(d[i])==1:
        max_len.append(*d[i])
for j in range(1,7):
    if res[j]==max_len[0]:
        min_len.append(abs(res[j-1]-res[j+1]))
        break
for j in range(1,7):
    if res[j]==max_len[1]:
        min_len.append(abs(res[j-1]-res[j+1]))
print((max_len[0]*max_len[1]-min_len[0]*min_len[1])*K)