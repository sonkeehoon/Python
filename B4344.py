C=int(input())
for _ in range(C):
    score=list(map(int,input().split(" ")))
    avg=sum(score[1:])/score[0]
    sum1=0
    for i in range(1,score[0]+1):
        if score[i]>avg:
            sum1+=1
    print(f"{(sum1/score[0])*100:.3f}%")