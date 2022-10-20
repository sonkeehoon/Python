def H_room(H,W,N):
    s=""
    if N//H>9:
        if N%H==0:
            s=str(H)+str(N//H)
        else:
            s=str(N%H)+str((N//H)+1)
    elif N//H==9:
        if N%H==0:
            s=str(H)+"0"+str(N//H)
        else:
            s=str(N%H)+str((N//H)+1)
    else:
        if N%H==0:
            s=str(H)+"0"+str(N//H)
        else:
            s=str(N%H)+"0"+str((N//H)+1)
    return s
T=int(input())
for i in range(T):
    H,W,N=map(int,input().split())
    print(H_room(H,W,N))