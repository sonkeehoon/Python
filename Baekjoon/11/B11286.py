# 절댓값 힙 : https://www.acmicpc.net/problem/11286
# 참고한 글 : https://velog.io/@treamor/Python-heapq-%EB%AA%A8%EB%93%88
# 내 블로그 : https://blog.naver.com/djfkfk12345/223284802887
import heapq
import sys
input = sys.stdin.readline

N = int(input()) # 연산의 개수
plus, minus = [], [] # 힙
for _ in range(N): 
    x = int(input()) # 연산에 대한 정보 x
    if x > 0:
        heapq.heappush(plus, x)
    elif x < 0:
        heapq.heappush(minus, -x)
        
    else:
        if plus and not minus: # minus 힙이 비어있으면
            print(heapq.heappop(plus))
        elif not plus and minus: # plus 힙이 비어있다면
            print(-heapq.heappop(minus))
        elif not plus and not minus: # 둘다 비어있으면 0
            print(0)
        else: # 둘다 비어있지 않다면
            # plus_min, minus_min = heapq.nsmallest(1, plus), heapq.nsmallest(1, minus)
            # plus_min, minus_min = min(plus), min(minus)
            plus_min, minus_min = heapq.heappop(plus), heapq.heappop(minus)
            if plus_min >= minus_min:
                print(-minus_min)
                heapq.heappush(plus, plus_min)
            else:
                print(plus_min)
                heapq.heappush(minus, minus_min)
            