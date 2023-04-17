# 2차원 리스트에서 부분리스트를 slicing해주는 코드
two_lst = [[i*5+j for j in range(1,6)] for i in range(5)]
print(*two_lst,sep='\n')
# 가운데 [7,8,9],[12,13,14],[17,18,19] 를 추출해보자
# (x1,y1) 부터 (x2,y2) 까지
x1, y1 = 1, 1 # 왼쪽 맨 위 7의 인덱스
x2, y2 = 3, 3 # 오른쪽 맨 아래 19의 인덱스
for i in range(x1,x2+1):
    print("[",end='')
    for j in range(y1,y2+1):
        if j < x2:
            print(two_lst[i][j],end=', ')
        else:
            print(two_lst[i][j],end='')
    print("]")
    

    
