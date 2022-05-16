S=input()
lst=[]
for i in range(1,len(S)+1):
    for j in range(len(S)-i+1):
        lst.append(S[j:i+j])
print(len(set(lst)))