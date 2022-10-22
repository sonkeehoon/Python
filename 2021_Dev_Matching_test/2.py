
def solution(rows, columns, queries):
    # from copy import deepcopy 
    # 복사본 생성할 때, 리스트의 크기가 큰 경우 
    # deepcopy 함수는 시간이 매우 오래걸린다. 
    # copy_m=[item[:] for item in 원본] 이러한 slicing 방식을 애용하도록 하자
    
    answer,res = [],[]
    m=[[columns*j+i+1 for i in range(columns)] for j in range(rows)]
    copy_m=[item[:] for item in m] # matrix의 복사본 생성
    for query in queries:
        x1=query[0]-1
        y1=query[1]-1
        x2=query[2]-1
        y2=query[3]-1
        for i in range(x1,x2+1):
            if i==x1:
                for j in range(y1,y2+1):
                    res.append(copy_m[i][j])
                    if j==y1:
                        m[i][j]=copy_m[i+1][j]
                        continue
                    m[i][j]=copy_m[i][j-1]
            elif x1<i<x2:
                m[i][y1]=copy_m[i+1][y1]
                m[i][y2]=copy_m[i-1][y2]
                res.append(copy_m[i][y1])
                res.append(copy_m[i][y2])
                
            elif i==x2:
                for k in range(y2,y1-1,-1):
                    res.append(copy_m[i][k])
                    if k==y2:
                        m[i][k]=copy_m[i-1][k]
                        continue
                    m[i][k]=copy_m[i][k+1]
        
        answer.append(min(res))
        res=[]
        copy_m=[item[:] for item in m]
        
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100,97,[[1,1,100,97]]))
