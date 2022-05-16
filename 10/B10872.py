def Fact(N):
    if N==0:return 1
    else:return N*Fact(N-1) 
print(Fact(int(input())))