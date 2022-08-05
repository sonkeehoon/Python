import re
print(re.match('Hello','Hello Python')) # 'Hello'와 'Hello Python' 두 문자열을 비교
a=re.search('is','My name is keehoon.') # 'My name is keehoon' 에서 'keehoon'이 있는지 판별 (없으면 None 출력)
if a==None:
    print('X')
else:
    print(a.group()) # group()메소드 : 'is'를 리턴
    print('O')

b=re.findall('H','Hi,IU. My name is KeeHoon. I\'m your fan')
if len(b)==0:
    print('단어가 없습니다')
else:
    print(b)
    
iters=re.finditer('s','assassinate')
for i in iters:
    print(i.span()) # span()함수 : 문자열 's'가 위치한 인덱스 범위를 리턴

o=re.fullmatch('abc','abc')
print(o.group())
