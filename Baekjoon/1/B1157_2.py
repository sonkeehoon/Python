from collections import Counter
word = input()
word = word.upper()
c = Counter(word).most_common()
if len(c) == 1:
    print(c[0][0])
elif c[0][1] == c[1][1]:
    print("?")
else:
    print(c[0][0])