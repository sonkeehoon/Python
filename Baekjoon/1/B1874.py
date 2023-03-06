import sys
input = sys.stdin.readline
n = int(input())
tmp = [i for i in range(n,0,-1)]
target = []
seq, seq2, res = [], [], []
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
        exit()
    i += 1
for r in res:
    print(r)