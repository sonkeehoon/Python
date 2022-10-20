N,W,H=map(int,input().split())
d=int((W**2+H**2)**0.5)
for i in range(N):
    l=int(input())
    if l<=d:
        print("DA")
        continue
    print("NE")