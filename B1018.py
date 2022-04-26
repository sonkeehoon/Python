M,N=map(int,input().split())
lst=[] # 입력값이 그대로 들어갈 리스트
lst2=[] # 한문자씩 들어갈 2차원 리스트
for i in range(M):
    lst.append(input())
    line=[]
    for j in range(N):
        line.append(lst[i][j])
    lst2.append(line)
for i in range(M):
    for j in range(N):
        if lst2[i][j]=='W':
            lst2[i][j]=True
        elif lst2[i][j]=='B':
            lst2[i][j]=False
cnt_lst=[] # 칠해야 하는 정사각형 갯수들의 모음
for k in range(M-8+1):
    for l in range(N-8+1):
        cnt=0
        mask,mask2=[],[] # 마스크, [0][0]번째 요소만 바꾼 마스크2
        for i in range(k,k+8):
            line=[]
            for j in range(l,l+8):
                line.append(lst2[i][j])
            mask.append(line)
        for i in range(0,8):
            if i!=0 and i%2==0 and mask[0][0]!=mask[i][0]:
                mask[i][0]=not(mask[i][0])
                cnt+=1
            elif i!=0 and i%2==1 and mask[0][0]==mask[i][0]:
                mask[i][0]=not(mask[i][0])
                cnt+=1
            for j in range(1,8):
                if j%2==0 and mask[i][0]!=mask[i][j]:
                    mask[i][j]=not(mask[i][j])
                    cnt+=1
                elif j%2==1 and mask[i][0]==mask[i][j]:
                    mask[i][j]=not(mask[i][j])
                    cnt+=1
        cnt_lst.append(cnt)
        cnt=1
        for i in range(k,k+8):
            line=[]
            for j in range(l,l+8):
                if i==k and j==l:
                    line.append(not(lst2[i][j]))
                    continue
                line.append(lst2[i][j])
            mask2.append(line)
        for i in range(0,8):
            if i!=0 and i%2==0 and mask2[0][0]!=mask2[i][0]:
                mask2[i][0]=not(mask2[i][0])
                cnt+=1
            elif i!=0 and i%2==1 and mask2[0][0]==mask2[i][0]:
                mask2[i][0]=not(mask2[i][0])
                cnt+=1
            for j in range(1,8):
                if j%2==0 and mask2[i][0]!=mask2[i][j]:
                    mask2[i][j]=not(mask2[i][j])
                    cnt+=1
                elif j%2==1 and mask2[i][0]==mask2[i][j]:
                    mask2[i][j]=not(mask2[i][j])
                    cnt+=1
        cnt_lst.append(cnt)
print(min(cnt_lst))
        
        
        
                    
            