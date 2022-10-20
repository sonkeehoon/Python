N=int(input())
first=N
cycle=0
while True:
    if N<10:
        N=10*N+N
        cycle+=1
        if N==first:
            print(cycle)
            break
        continue
    N=10*(N%10)+(N//10+N%10)%10
    cycle+=1
    if N==first:
        print(cycle)
        break
input()