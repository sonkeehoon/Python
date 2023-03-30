# B진법 수 N을 10진법으로 바꿔야함
N,B =input().split()
B = int(B)

total = 0
for idx,n in enumerate(N[::-1]): # n 은 문자열N의 한 글자
    
    tmp = B**idx # 진법수의 자릿수만큼 제곱
    if n.isdigit(): # n이 0~9 인경우는 숫자로 취급한다
        total += int(n)*tmp
        continue
    
    # n이 알파벳인 경우 아닐경우 처리
    total += (ord(n) - 55)*(tmp)
    
print(total)
    
    

