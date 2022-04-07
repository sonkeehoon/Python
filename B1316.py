N=int(input())
lst=[0]*N
for i in range(N):
    lst[i]=input()
for w in lst:
    cnt=1
    for j in range(len(w)-1):
        if w[j]==w[j+1]:
            cnt+=1
        else:
            if w.count(w[j])==cnt:
                cnt=1
            else:
                cnt=1
                N-=1
                break
print(N)
                
            
            
            
        
        
        
        
            
            
        
    
    
    