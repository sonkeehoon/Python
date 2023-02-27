# 쉬운 문제인줄 알았는데.. 생각보다 오래 걸렸다
# chr(65) : 'A', ord('A') : 65
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    num = 0
    queue = deque(map(int,input().split()))
    queue2 = deque([chr(i) for i in range(65,65+N)])
    target = queue2[M] # 몇번째로 인쇄되는지 알아야 하는 문서
    d = {}
    for i in range(len(queue)):
        d[queue2[i]] = queue[i]

    while queue:
        max_val = max(queue)
        if d[queue2[0]] == max_val:
            queue.popleft()
            tmp = queue2.popleft()
            num += 1
            if tmp == target:
                print(num)
                break
        else:
            queue.rotate(-1)
            queue2.rotate(-1)

            
            
            
            
            
                
        
        
        
                
        
            
        
        
            
        
            
            
    
    
    