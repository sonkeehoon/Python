# 3. 다단계 칫솔 판매 : https://school.programmers.co.kr/learn/courses/30/lessons/77486
# 언제쯤 풀거니 기훈아..?? ㅎㅎ
# 시간은 오래 걸렸는데 그래도 스스로 풀어냈다 (뿌듯)

# enroll이 입력, referral이 부모, seller은 판매자
def solution(enroll, referral, seller, amount):
    
    result = [0] * len(enroll)
    
    amount = list(map(lambda x: x * 100, amount))
    d={}
    profit_d={}
    for i in range(len(enroll)):
        en=enroll[i]
        d[en] = referral[i]
        profit_d[en]=i
        
    for idx,s in enumerate(seller):
        e = s
        x = amount[idx]
        while x>=1:
            # print(result)
            p = d[e]
            if p == "-":
                result[profit_d[e]] += x - x//10
                break
            
            result[profit_d[e]] += x - x//10
            
            x= x//10
            e = p
    return result

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
         ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
         ["young", "john", "tod", "emily", "mary"],
         [12, 4, 2, 5, 10]))