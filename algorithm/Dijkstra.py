# 최단 경로를 찾는 알고리즘
# start에서 각 점까지 가는 최단 경로를 구해준다 (갈수 없는경우 INF)
# queue로 구현해봤지만 효율성을 높이려면 heapq로 구현하면 된다
# 참고 사이트(그래프) : https://it-garden.tistory.com/m/241
import sys
INF = sys.maxsize
# input = sys.stdin.readline

adjacent = [{}, {2:2, 3:3, 4:6}, {6:4}, {4:1}, {}, {}, {}]
start = int(input("시작 점을 입력하세요 : "))
dist = [INF] * len(adjacent)
dist[start] = 0
queue = []
queue.append([0,start]) # 시작점으로 가는 길이 0

while queue:
    here = queue.pop()[1]
    
    for there,length in adjacent[here].items():
        print(here, there, length)
        next_dist = dist[here] + length
        
        if next_dist < dist[there]:
            print('if')
            dist[there] = next_dist
            queue.append([there, next_dist])
        print(dist,queue)
print(dist[1:])
    
    