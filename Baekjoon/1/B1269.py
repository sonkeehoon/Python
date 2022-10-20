import sys
input=sys.stdin.readline
na,nb=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A=set(A)
B=set(B)
AB=A-B
BA=B-A
print(len(AB.union(BA)))



    