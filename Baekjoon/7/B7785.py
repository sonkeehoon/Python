import sys
input = sys.stdin.readline
n = int(input())
d = {}

for _ in range(n):
    name, state = input().split()
    if state == "enter": # 출근 상태면
        d[name] = True
    elif state == "leave":
        del d[name]
print(*sorted(d.keys(), reverse=True), sep='\n')

# 딕셔너리 ,집합 여러가지 방식으로 풀어봤는데 
# 메모리와 시간을 가장 적게(효율적으로)쓰려면 딕셔너리가 정답이었다
# enter일때 이름을 딕셔너리에 넣고 leave면 빼는 방식
# 깨달은점 : set에 sorted를 쓰면 정렬해서 list로 반환(집합에 sort연산은 불가능!)

