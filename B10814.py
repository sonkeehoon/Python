import sys
N=int(sys.stdin.readline())
lst=[sys.stdin.readline().split() for i in range(N)]
lst=[(int(i[0]),i[1]) for i in lst]
lst=sorted(lst,key=lambda x: (x[0]))
for i in lst:
    print(i[0],i[1])