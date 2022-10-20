s=input()
d=["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in range(len(d)):
    if d[i] in s:
        s=s.replace(d[i],"#")
print(len(s))
        
        

