T=int(input())
for _ in range(T):
    R,S=map(str,input().split(" "))
    for i in range(len(S)):
        print(S[i]*int(R),end="")
    print()