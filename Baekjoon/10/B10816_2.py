def binary_search(arr, target): # arr은 배열, target은 찾고자 하는 값
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # 중간 인덱스 계산

        if arr[mid] == target:
            return c[target] # 원하는 요소를 찾았을 때
        elif arr[mid] < target: # target이 중간값보다 크면
            left = mid + 1  # 중간 값보다 큰 부분에서 다시 검색
        else: # target이 중간값보다 작으면
            right = mid - 1  # 중간 값보다 작은 부분에서 다시 검색

    return 0  # 요소를 찾지 못한 경우 -1 반환

from collections import Counter
import sys
input = sys.stdin.readline
N = int(input()) # 숫자 카드의 개수
card = list(map(int, input().split())) # 숫자 카드에 적혀있는 정수
M = int(input()) 
targets = list(map(int, input().split())) # card에 있는지 판별하고자 하는 M개의 정수
card.sort()
c= Counter(card)

for target in targets:
    tmp = binary_search(card, target)
    print(tmp, end=' ')
    
    
    
    
        
    




