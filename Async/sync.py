# 동기적인 코드 예시
import time
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)
    print("end")

def print_numbers2():
    for i in range(6, 11):
        print(i)
        time.sleep(1)
    print("end")

def main():
    print_numbers()
    print_numbers2()
    print("All numbers printed.")

main()
