
s=str(input())
cnt=0
for i in range(len(s)-1): # 공백이 연속으로 나오는지 검사
    if s[i]==" " and s[i+1] ==" ":
        exit()
if s[0]==" ":
    if s[len(s)-1]==" ":
        cnt=s.count(" ")-1
    else:
        cnt=s.count(" ")
else:
    if s[len(s)-1]==" ":
        cnt=s.count(" ")
    else :
        cnt=s.count(" ")+1
print(cnt)