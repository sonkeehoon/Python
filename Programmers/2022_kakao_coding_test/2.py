def solution(teamK, teamB):
    res=[0]*len(teamB)
    K=len(teamK)
    M=max(teamK)
    for B in teamB:
        if B>=M:
            res.append(K)
            continue
        cnt=0
        for i in range(K):
            if teamK[i]<=B:
                cnt+=1
        res.append(cnt)
        
    return res
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    teamK_count = int(input().strip())

    teamK = []

    for _ in range(teamK_count):
        teamK_item = int(input().strip())
        teamK.append(teamK_item)

    teamB_count = int(input().strip())

    teamB = []

    for _ in range(teamB_count):
        teamB_item = int(input().strip())
        teamB.append(teamB_item)

    result = solution(teamK, teamB)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
    print(result)