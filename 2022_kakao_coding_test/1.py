def solution(X, arr, indexes):
    lst=[]
    if X not in arr:
        return len(indexes)*[-1]
    for i in range(len(arr)):
        if arr[i]==X:
            lst.append(i)
    res=[]
    for idx in indexes:
        if len(lst)<idx:
            res.append(-1)
            continue
        res.append(lst[idx-1]+1)
    return res  
if __name__ == '__main__':

    X = int(input().strip())

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    indexes_count = int(input().strip())

    indexes = []

    for _ in range(indexes_count):
        indexes_item = int(input().strip())
        indexes.append(indexes_item)

    result = solution(X, arr, indexes)
    print(result)