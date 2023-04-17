# 피보나치 수 6 : https://www.acmicpc.net/problem/11444
# 스스로 해결 여부 : X

n = int(input())
# divisor = 1000000007
divisor = 41

F = [0,1] + [0]*(n-1)
for i in range(2, len(F)):
    F[i] = (F[i-2] + F[i-1])%divisor
print(F[:n])
        
