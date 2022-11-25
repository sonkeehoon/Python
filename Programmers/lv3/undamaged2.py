
def solution(board, skill):
    answer = 0
    # board는 2차원 배열
    # type 1: 공격 2: 회복
    I, J = len(board), len(board[0])
    lst = [[0 for _ in range(J+1)] for _ in range(I+1)]
    
    
    for sk in skill:
        type = sk[0]
        r1, c1 = sk[1], sk[2]
        r2, c2 = sk[3], sk[4]
        degree = sk[5]
        
        if type == 1: # 공격
            lst[r1][c1] -= degree
            lst[r1][c2+1] += degree
            lst[r2+1][c1] += degree
            lst[r2+1][c2+1] -= degree              
        elif type == 2: # 회복
            lst[r1][c1] += degree
            lst[r1][c2+1] -= degree
            lst[r2+1][c1] -= degree
            lst[r2+1][c2+1] += degree
    print(lst)
    # 옆으로
    for i in range(I):
        num = 0
        for j in range(J):
            lst[i][j] += num
            num = lst[i][j]
    # 위에서 아래로
    for j in range(J):
        num = 0
        for i in range(I):
            lst[i][j] += num
            num = lst[i][j]
            
            
    for i in range(I):
        for j in range(J):
            if board[i][j] + lst[i][j] > 0:
                answer += 1     
                
    return answer

print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))