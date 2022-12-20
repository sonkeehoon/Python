# input : sample.txt
# output : result.txt


# import re # 2번 방법에서 활용할 re모듈
from collections import Counter

def print_result(target):
    global start
    end = len(target)
    print(end)
    print(f"{start-end} 개의 단어가 삭제되었습니다.")
    
# 긴 문자열 불러오기
f = open("./sample.txt", "r", encoding = "utf8")
lines = f.read()
start = len(lines)
print(start)
f.close()

# 지웠으면 하는 문자 : "-[]~`'!@#$%^&*()_+ ●.\n"
erase_words = """‘_:"/\|?<>;}{()=,-[]~`'!@#$%^&*()_+ ●.\n …※˚✧₊⁎⁺˳✧༚･"""


# 1. for문과 replace를 활용
target = lines
for word in erase_words:
    target = target.replace(word, "")
target = target.replace("문서", "")
target = target.replace("저장하기", "")
print_result(target)

# 2. re.sub 활용 (개인적으론 별로인 방법.. 정규표현식을 안 좋아해서 그런걸지도)
# target = lines
# target = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s] ", "", target) # 정규표현식 공부가 따로 필요하다
# target = target.replace("문서", "")
# target = target.replace("저장하기", "")
# print_result(target)

# 3. maketrans, translate 활용
target = lines
transtable = target.maketrans("", "", erase_words)
target = target.translate(transtable)
target = target.replace("문서", "")
target = target.replace("저장하기", "")
print_result(target)

# 문자열에 특정문자가 있는지 판단하기
print("123".isdigit())
print("hello".isalpha())
print("keehoon9312".isalnum())
print(Counter(target))

# result.txt에 결과텍스트 저장
f = open("./result.txt", "w", encoding = "utf8")
f.write(target)
f.close()