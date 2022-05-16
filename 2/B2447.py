import time
import sys
N=int(sys.stdin.readline())
start=time.time()
def star(N):
    lst=[]
    if N==3:return [["*","*","*"],["*"," ","*"],["*","*","*"]]
    s=star(N//3)
    for i in range(3):
        for j in range(N//3):
            if i==1:
                lst.append(s[j]+[' ']*(N//3)+s[j])
                continue
            lst.append(s[j]*3)
    return lst
for i in star(N):
    for j in i:
        sys.stdout.write(j)
    sys.stdout.write('\n')
print("time is {:.3f}".format(time.time()-start))