two_lst = [[i*5+j for j in range(1,6)] for i in range(5)]
print(*two_lst,sep='\n')
# 가운데 [7,8,9],[12,13,14],[17,18,19] 를 추출해보자
# (1,1) 부터 (3,3) 까지
for i in range(1,4):
    print("[",end='')
    for j in range(1,4):
        if j < 3:
            print(two_lst[i][j],end=', ')
        else:
            print(two_lst[i][j],end='')
    print("]")
    

    
