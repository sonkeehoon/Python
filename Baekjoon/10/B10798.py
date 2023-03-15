words = []
for _ in range(5):
    words.append(input())
len_lst =[]
for word in words: # 각 행의 길이들의 최댓값 구하기
    len_lst.append(len(word))

for i in range(max(len_lst)):
    for j in range(len(words)):
        try: print(words[j][i],end='')
        except: continue

        