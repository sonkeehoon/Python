# 가장 긴 증가하는 부분 수열 2 : https://www.acmicpc.net/problem/12015

import sys
input = sys.stdin.readline

N = int(input()) # len(A)
A = list(map(int,input().split()))
LIS = [A[0]]

def binary_search(LIS: list, item: int):
    left, right = 0, len(LIS)
    
    while left <= right:
        mid = (left + right) // 2
        if LIS[mid] == item:
            return mid
        
        elif LIS[mid] > item:
            right = mid - 1
            
        else:
            left = mid + 1
            
    return left # 가장 처음 item보다 같거나 커지는 시점의 인덱스

for item in A[1:]:
    if LIS[-1] < item:
        LIS.append(item)
        
    elif LIS[-1] > item:
        idx = binary_search(LIS, item)
        LIS[idx] = item
        
print(len(LIS))
    
        
        
    
    