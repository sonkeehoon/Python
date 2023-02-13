# (틀린문제)나중에 재시도 해보자
import sys
from collections import deque
input = sys.stdin.readline
n = int(input().strip())
target,res,tmp = [],[],[]
seq = deque(i for i in range(1, n+1))

for _ in range(n):
    target.append(int(input().strip()))
target = list(reversed(target))
lst = []
x = 0
for idx,t in enumerate(target):
    if len(seq) == 0:
        if tmp[-1] != t:
            seq = deque(reversed(tmp))
            tmp = []
            while lst:
                seq.appendleft(lst.pop())
                res.append('-')
            break
        tmp.append(lst.pop())
        res.append('-')
        
    else:
        if seq[0] == t:
            lst.append(seq.popleft())
            res.append('+')
            continue
        elif seq[0] < t:
            while seq[0] != t:
                lst.append(seq.popleft())
                res.append('+')
            while target[idx-1] != lst[-1]:
                tmp.append(lst.pop())
                res.append('-')
            lst.append(seq.popleft())
            res.append('+')
        else:
            print("NO")
            break
print(seq,lst,tmp,res)
if list(seq) == target:
    for r in res:
        print(r)
    

    