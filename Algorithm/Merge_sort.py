# 코드 이해하기가 어려웠다.. 이런 방법도 있구나 하고 넘어갈 생각이다.
# 참고한 코드 : https://my-coding-notes.tistory.com/581
import sys
input = sys.stdin.readline

def merge_sort(A):
    l = len(A)
    if l == 1:
        return A
    
    mid = (l+1)//2
    
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    
    i, j = 0, 0
    lst = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            ans.append(right[j])
            j += 1
    while i < len(left):
        lst.append(left[i])
        ans.append(left[i])
        i += 1
    while j < len(right):
        lst.append(right[j])
        ans.append(right[j])
        j += 1
    
    return lst
            
N, K = map(int,input().split())
A = list(map(int,input().split()))
ans = []
merge_sort(A)

if len(ans) >= K:
    print(ans[K-1])
else:
    print(-1)
    