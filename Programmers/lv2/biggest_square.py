# 가장 큰 정사각형 찾기 : https://school.programmers.co.kr/learn/courses/30/lessons/12905
def solution(board):
    row = len(board)
    column = len(board[0])
    
    for i in range(1, row):
        for j in range(1, column):
            if board[i][j] == 1 :
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    
    m = []
    for b in board:
        m.append(max(b))
        
    return (max(m))**2   

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))