# (틀린문제)나중에 재시도 해보자(실버2)
# 재시도 후 통과했다!
# 이해가 안될때는 연습장에 쓰면서 해보는것도 좋은방법 같다.
# 스택에 push하는 순서는 반드시 오름차순
# push : +, pop : -
import sys
input = sys.stdin.readline
n = int(input())
tmp = [i for i in range(n,0,-1)]
target = []
seq, seq2, res = [], [], []
avail=True
for _ in range(n): # 1이상 n이하의 정수가 하나씩 순서대로
    target.append(int(input()))
i = 0
while tmp or seq:
    while len(tmp) > 0 and target[i] >= tmp[-1]:
        seq.append(tmp.pop())
        res.append('+')
    while len(seq) > 0 and target[i] == seq[-1]:
        seq2.append(seq.pop())
        res.append('-')
    if len(seq) > 0 and target[i] < seq[-1]:
        print("NO")
        avail=False
        break
    i += 1
if avail:
    for r in res:
        print(r)
    
        
    
    