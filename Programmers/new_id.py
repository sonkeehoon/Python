# 정규 표현식 예제
import re
def solution(new_id):
    
    # new_id의 모든 대문자를 대응되는 소문자로 치환
    new_id = new_id.lower()
    print(new_id)
    
    # new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    new_id = re.sub('[^a-z\d\-\_\.]','',new_id)
    print(new_id)
    
    # new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    new_id=re.sub('\.\.+','.',new_id)
    print(new_id)
    
    # new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거
    new_id=re.sub('^\.|\.$','',new_id)
    print(new_id)
    
    # new_id가 빈 문자열이라면, new_id에 "a"를 대입
    if len(new_id)==0:
        new_id='a'
    print(new_id)
    
    # new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    new_id = re.sub('\.$','',new_id[0:15])
    print(new_id)
    
    # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙이기
    while len(new_id)<3:
        new_id+=new_id[-1:]
    print(new_id)
    
    return new_id
    

solution("abcdefghijklmn.p")