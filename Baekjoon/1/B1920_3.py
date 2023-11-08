# 수 찾기 : https://www.acmicpc.net/problem/1920
# 앞서 풀었던 코드(리스트에 in 으로 해결)와 다르게 이번엔 이진탐색을 사용한다

def binary_search(arr, target): # arr은 배열, target은 찾고자 하는 값
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # 중간 인덱스 계산

        if arr[mid] == target:
            return 1  # 원하는 요소를 찾았을 때 인덱스 반환
        elif arr[mid] < target: # target이 중간값보다 크면
            left = mid + 1  # 중간 값보다 큰 부분에서 다시 검색
        else: # target이 중간값보다 작으면
            right = mid - 1  # 중간 값보다 작은 부분에서 다시 검색

    return 0  # 요소를 찾지 못한 경우 -1 반환

import sys
input = sys.stdin.readline
N = int(input()) # arr에 들어갈 배열
A = list(map(int,input().split()))
M = int(input()) # target 값들이 들어있는 배열
A.sort()

targets = list(map(int,input().split()))

for target in targets:
    print(binary_search(A, target))


