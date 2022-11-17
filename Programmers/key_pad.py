# 키패드 누르기 : https://school.programmers.co.kr/learn/courses/30/lessons/67256
# 미해결 60 / 100
def solution(numbers, hand):
    answer=""
    left,right="*","#"
    pad={1:[1,1],2:[1,2],3:[1,3],
         4:[2,1],5:[2,2],6:[2,3],
         7:[3,1],8:[3,2],9:[3,3],
         "*":[4,1],0:[4,2],"#":[4,3]}
    for n in numbers:
        if n in [1,4,7]:
            answer+="L"
            left=n
        elif n in [3,6,9]:
            answer+="R"
            right=n
        else:
            ld=(pad[left][0]-pad[n][0])**2+(pad[left][1]-pad[n][1])**2
            rd=(pad[right][0]-pad[n][0])**2+(pad[right][1]-pad[n][1])**2
            if ld<rd:
                answer+="L"
                left=n
            elif ld>rd:
                answer+="R"
                right=n
            else:
                if hand=="right":
                    answer+="R"
                    right=n
                elif hand=="left":
                    answer+="L"
                    left=n

    return answer
                    
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right")
