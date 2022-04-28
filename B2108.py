import sys
import statistics
inp=sys.stdin.readline
N=int(inp())
lst=[]
for i in range(N):
    lst.append(int(inp()))
lst.sort()
most_freq=0
mode=statistics.multimode(lst)
mode.sort()
if len(mode)==1:
    most_freq=mode[0]
else:
    most_freq=mode[1]
print(round(sum(lst)/N),lst[int((N-1)//2)],most_freq,max(lst)-min(lst),sep='\n')
