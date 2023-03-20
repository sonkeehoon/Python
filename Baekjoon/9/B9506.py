import sys
input = sys.stdin.readline
while True:
    lst = []
    n = int(input())
    if n == -1:
        break
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            lst.append(n//i)
            lst.append(i)
    lst = sorted(list(set(lst))) # 중복 제거하고 정렬
    lst.pop() # 자기 자신은 빼버리기
    if n == sum(lst):
        print(f"{n} = ",end="")
        print(' + '.join(list(map(str,lst))))
        
        continue
    print(f"{n} is NOT perfect.")
        
            
        
    