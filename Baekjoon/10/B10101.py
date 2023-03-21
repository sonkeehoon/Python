angles = []
for _ in range(3):
    angles.append(int(input()))

tmp = sum(angles)
l = len(set(angles))
if angles[0] == angles[1] == angles[2] == 60:
    print("Equilateral")
elif tmp == 180 and l == 2:
    print("Isosceles")
elif tmp == 180 and l == 3:
    print("Scalene")
elif tmp != 180:
    print("Error")