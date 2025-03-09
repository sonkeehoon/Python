# 2차원 리스트에서 부분리스트를 slicing해주는 코드

    
# 가운데 [7,8,9],[12,13,14],[17,18,19] 를 추출해보자
# (x1,y1) 부터 (x2,y2) 까지

def get_sublist(lst: list, 
                 x1: int, y1: int, 
                 x2: int, y2:int )-> list:
    
    sublist = []
    
    if x2 >= len(lst) or y2 >= len(lst[0]) or x1 < 0 or y1 < 0:
        raise ValueError("잘못된 값입니다!")
    if any(( type(coord) != int for coord in [x1, x2, y1, y2] )):
        raise TypeError("자연수만 입력하세요!")
        
    for i in range(x1, x2+1):
        line = []
        
        for j in range(y1, y2+1):
            if j < x2:
                line.append(lst[i][j])
                
            else:
                line.append(lst[i][j])
        
        sublist.append(line)
    
    return sublist

if __name__ == "__main__":
    init_lst = [[i*5+j for j in range(1,6)] for i in range(5)]
    print(*init_lst,sep='\n')
    print()
    res = get_sublist(init_lst, 1, 1, 4, 3)
    print(res)
    

    
