
def solution(rows, columns, queries):
    import copy
    
    answer = []
    matrix=[[rows*j+i+1 for i in range(rows)] for j in range(columns)]
    copy_m=copy.deepcopy(matrix) # matrix의 복사본 생성
    for query in queries:
        x1=query[0]-1
        y1=query[1]-1
        x2=query[2]-1
        y2=query[3]-1
        # for i in range(y1,y2+1):
        #     if i==0 or i==
        #     for j in range(x1,x2+1):
        
        
        
        
    return answer

solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])