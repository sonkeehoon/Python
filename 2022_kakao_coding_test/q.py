import sys
def solution(survey,choices):
    d={}
    d['R']=0
    d['T']=0
    d['C']=0
    d['F']=0
    d['J']=0
    d['M']=0
    d['A']=0
    d['N']=0
    for i in range(len(survey)):
        if choices[i]<4:
            d[survey[i][0]]+=4-choices[i]
        elif 4<choices[i]<=7:
            d[survey[i][1]]+=choices[i]-4
        elif choices[i]==3:
            pass
    res=""
    if d['R']>d['T']: res+='R'
    elif d['R']<d['T']: res+='T'
    else: res+=sorted('RT')[0]
    
    if d['C']>d['F']: res+='C'
    elif d['C']<d['F']: res+='F'
    else: res+=sorted('CF')[0]
    
    if d['M']>d['J']: res+='M'
    elif d['M']<d['J']: res+='J'
    else: res+=sorted('MJ')[0]
    
    if d['A']>d['N']: res+='A'
    elif d['A']<d['N']: res+='N'
    else: res+=sorted('AN')[0]

    return res
survey=[""] # 질문마다 판단하는 지표를 담은 문자열 배열
choices=[] # 선택지를 담은 정수 배열 (i+1번째 질문의 선택지,검사자가 선택한 응답 1~7)
survey=sys.stdin.readline().strip()
choices=sys.stdin.readline().strip()
survey=survey[1:-1].replace('"',' ')
survey=survey.replace(' ','').strip()
survey=survey.split(',')
print(choices)
choices=list(map(int,choices[1:-1].split(',')))
print(survey,choices)
# final_res=solution(survey,choices)
# print('"'+final_res+'"')