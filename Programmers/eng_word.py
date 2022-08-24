def solution(s):
    answer = 0
    d={"zero" : "0",
        "one" : "1", "two" : "2", "three" : "3",
        "four" : "4", "five" : "5", "six" : "6",
        "seven" : "7", "eight" : "8", "nine" : "9"}
    for n in d.keys():
        if n in s:
            s = s.replace(n,d[n])
    answer=int(s)
    return answer

print(solution("2three45sixseven"))