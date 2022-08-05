import re
def solution(new_id):
    new_id = new_id.lower()
    print(new_id)
    
    new_id = re.sub('[^a-z\d\-\_\.]','',new_id)
    print(new_id)
    
    new_id=re.sub('\.\.+','.',new_id)
    print(new_id)
    
    new_id=re.sub('^\.|\.$','',new_id)
    print(new_id)
    
    if len(new_id)==0:
        new_id='a'
    print(new_id)
    
    new_id = re.sub('\.$','',new_id[0:15])
    print(new_id)
    
    while len(new_id)<3:
        new_id+=new_id[-1:]
    print(new_id)
    
    return new_id
    

solution("abcdefghijklmn.p")