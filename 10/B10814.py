import sys
N=int(sys.stdin.readline())
lst=[sys.stdin.readline().split() for i in range(N)] # 2차원 리스트에 저장
lst=[(int(i[0]),i[1]) for i in lst] # 나이값들만 정수로 변환
lst=sorted(lst,key=lambda x: (x[0])) # 리스트 각요소의 0번째 요소를 ket(기준)으로 정렬
for i in lst:
    print(i[0],i[1])