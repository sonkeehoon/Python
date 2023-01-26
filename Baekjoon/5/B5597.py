import sys
input = sys.stdin.readline
number = 30 # 전체 학생 수
num = 28 # 과제 제출한 학생 수
students_num = [i+1 for i in range(number)]
for i in range(num):
    n = int(input())
    students_num.remove(n)
print(*students_num,sep='\n')
    