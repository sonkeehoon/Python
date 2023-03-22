# 어디에 써먹을지는 모르겠지만.. 갑자기 그냥 만들어봤다
# 텍스트의 빈도 분석을 해주는 그런 프로그램..
from collections import Counter
# import numpy as np
import pandas as pd

def del_all_char_inList(txt : list, target):
    while target in txt:
        txt.remove(target)
    return txt

# 텍스트를 불러오고 단어별로 list에 담는다(공백을 기준으로 한 단어로 취급)
with open('./tech_list.txt',"r",encoding="utf-8") as f:
    txt = f.readlines() # 불러온 텍스트를 저장할 리스트 txt
    txt2 =[] # txt를 단어별로 분리해서 담을 리스트 txt2
    for idx,t in enumerate(txt): # 개행문자들을 없애고 공백을 기준으로 분리해서 txt2에 담는다
        txt[idx] = t.rstrip('\n')
        tmp = txt[idx].split(' ')
        txt2 += tmp

# 특수문자 같은 쓸데없는 단어들을 리스트에서 전부 삭제하자
target_string = ['',' ' '-', ',', ')', '(', ':', '\\', '/', '[', ']' ]
for string in target_string:
    del_all_char_inList(txt2, string)

c = Counter(txt2) # txt2의 Counter객체를 담을 c
# print(c)

# 입력받은 문자가 몇개 있는지 알려주기
ipt = input("찾고싶은 단어가 있으신가요?\n하나의 단어를 입력하세요 : ")
if c[ipt] == 0:
    print(f"'{ipt}'은(는) 텍스트에 없네요")
else:
    print(f"'{ipt}'은(는) {c[ipt]}개 있습니다")

answer = input("\n전체 빈도수를 저장할까요?(Y/N) ")
if answer == 'Y' or answer == 'y':
    print(c)
    a = list(c.keys())
    b = list(c.values())
    data = pd.DataFrame({"word" : a, "frequency" : b})
    data = data.sort_values(by = "frequency", ascending = False)
    data.to_csv('data.csv', sep='\t', index=False, encoding="utf-8-sig")


print("\nbye!")