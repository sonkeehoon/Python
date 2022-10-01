import re
# git hub test
print(re.match('llo','Hello Python')) # 'Hello'와 'Hello Python' 두 문자열을 비교 (맨 첫 문자부터 같아야함)
a=re.search('is','My name is keehoon.') # 'My name is keehoon' 에서 'keehoon'이 있는지 판별 (없으면 None 출력)
if a==None:
    print('X')
else:
    print(a) # group()메소드 : 'is'를 리턴, span() : is의 위치 인덱스를 리턴
    print('O')
print('is' in 'My name is keehoon.')

b=re.findall('H','Hi,IU. My name is KeeHoon. I\'m your fan')  # 'H'가 몇번 나오는지 확인할때
if len(b)==0:
    print('단어가 없습니다')
else:
    print(len(b))
    
iters=re.finditer('s','assassinate') # 문자열 's'를 모두 찾아서 인덱스를 저장
for i in iters:
    print(i.span()) # span()함수 : 문자열 's'가 위치한 모든 인덱스 범위를 리턴

o=re.fullmatch('abc','abc')
print(o.group())
