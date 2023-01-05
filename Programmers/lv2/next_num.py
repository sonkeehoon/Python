def solution(n):
    num_one = bin(n).count('1')
    while True:
        n += 1
        if num_one == bin(n).count('1'):
            return n

print(solution(15))