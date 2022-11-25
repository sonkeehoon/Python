# 파괴되지 않은 건물 : https://school.programmers.co.kr/learn/courses/30/lessons/92344
# 첫 시도 : 53.8 / 100.0 (정확성 테스트 통과, 효율성 테스트 탈락)
# 누적합 개념을 적용해야만 시간을 효과적으로 줄이면서 효율성 테스트까지 통과할 수 있었다
# 두번째 시도 : https://blog.naver.com/eternalklaus/222745635421 이곳의 풀이와
# https://nicotina04.tistory.com/163의 imos 알고리즘을 참고해서 풀었다
# 그 다음 내 코드에 적용해봄. 이걸 혼자서 생각해 내는건 내 머리로는 불가능할것 같다
# 누적합 개념을 익히는 경험으로 생각하자

def solution(board, skill):
    answer = 0
    # board는 2차원 배열
    # type 1: 공격 2: 회복
    for sk in skill:
        type = sk[0]
        r1, c1 = sk[1], sk[2]
        r2, c2 = sk[3], sk[4]
        degree = sk[5]
        
        if type == 1: # 공격
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] -= degree
                    
        elif type == 2: # 회복
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] += degree
    for b in board:
        for k in b:
            if k>0:
                answer += 1 
                
    return answer

solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])