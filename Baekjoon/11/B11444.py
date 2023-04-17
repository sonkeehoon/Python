# 피보나치 수 6 : https://www.acmicpc.net/problem/11444
# 스스로 해결 여부 : X
# 이 문제를 풀기 위해 B1629.py를 다시 풀었다
# 분할정복과 이차원행렬 곱셈을 알아야 풀수 있는 문제다
# 문제가 어려워서 남의 코드를 붙여넣기 하고 종이에 써가면서 로직만 이해했다
# 참고 : https://cantcoding.tistory.com/28

# 제곱
def power(f,n):
    if n == 1:
        return f
    elif n % 2 == 0: # 짝수면
        return power(multi(f,f),n//2)
    else: # 홀수면
        return multi(power(f,n-1),f)
    
def multi(a,b): # 2차원 행렬 a와 b를 곱해주는 함수
    tmp = [[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k] * b[k][j]
            tmp[i][j] = sum % div # 미리나눠서 tmp에 더해줌
    return tmp

n = int(input())
f = [[1,1],[1,0]]
start = [[1],[1]]
div = 1000000007

if n < 3: 
    print(1)
else: # n >= 3
    print(multi(power(f, n-2), start)[0][0])
    
    


        
        


        
