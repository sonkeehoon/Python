# 숨바꼭질: https://www.acmicpc.net/problem/1697
import sys
input = sys.stdin.readline
N, K = map(int, input().split())

# dfs 활용 풀이(효율 좋음)
from collections import deque
q = deque()
visited = set()
MAX = int(1e5)

q.append((N, 0))
visited.add(N)

if N >= K :
    print(N - K)

else: 
    while q:
        cur_pos, cur_time = q.popleft()
        
        if cur_pos == K:
            print(cur_time)
            break        
        
        if cur_pos - 1  >= 0 and cur_pos - 1 not in visited:
            visited.add(cur_pos - 1)
            q.append((cur_pos - 1, cur_time + 1))
        
        if cur_pos < K:
            if 2*cur_pos <= MAX and 2*cur_pos not in visited:
                visited.add(2*cur_pos)
                q.append((2*cur_pos, cur_time + 1))
                
            if cur_pos + 1 < MAX and cur_pos + 1 not in visited:
                visited.add(cur_pos + 1)
                q.append((cur_pos + 1, cur_time + 1))

# # dp 풀이(통과, 효율 안좋음)
# INF = float("inf")
# MAX = int(1e7)
# dp = [INF for _ in range(MAX)]
# dp[N] = 0
# s = {N}
# if N >= K:
#     print(N - K)

# else:
#     while K not in s:
#         tmp = set()
#         for e in s:
#             print(e)
#             if dp[e - 1] == INF:
#                 tmp.add(e - 1)
#                 dp[e - 1] = dp[e] + 1
#                 if e - 1 == K:
#                     break
#             if e < K:
#                 if dp[e + 1] == INF:
#                     tmp.add(e + 1)
#                     dp[e + 1] = dp[e] + 1
#                     if e + 1 == K:
#                         break
#                 if dp[2*e] == INF:
#                     tmp.add(2*e)
#                     dp[2*e] = dp[e] + 1
#                     if 2*e == K:
#                         break
                    
#         s = tmp

#     print(dp[K])


