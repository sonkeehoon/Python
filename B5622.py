w=input()
t=0
for i in range(len(w)):
        if ord(w[i])<=76:
            if ord(w[i])<=70:
                if ord(w[i])<=67: t+=3;continue
                else: t+=4;continue
            else : 
                if ord(w[i])<=73: t+=5;continue
                else: t+=6;continue
        else :
            if ord(w[i])<=83:
                if ord(w[i])<=79: t+=7;continue
                else: t+=8;continue
            else :
                if ord(w[i])<=86: t+=9;continue
                else: t+=10;continue
print(t)   
