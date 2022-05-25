import sys
input=sys.stdin.readline
T=int(input())
for i in range(T):
    x1,y1,x2,y2=map(int,input().split())
    n=int(input())
    cnt=0
    for _ in range(n):
        cx,cy,r=map(int,input().split())
        if (x1-cx)**2+(y1-cy)**2<r**2 and (x2-cx)**2+(y2-cy)**2<r**2:
            continue
        elif (x1-cx)**2+(y1-cy)**2<r**2:
            cnt+=1
        elif (x2-cx)**2+(y2-cy)**2<r**2:
            cnt+=1
    print(cnt)
# 아이디어는 다른사람의 소스를 참고했습니다.
# 다른사람의 소스 : https://www.acmicpc.net/board/view/79098
# 두 점 사이의 거리를 구할때 math.dist도 사용 가능
