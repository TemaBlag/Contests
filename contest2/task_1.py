countShumerid = int(input())
countCube = 0
countDelCube = 0
for i in range(1, countShumerid + 1):
    countCube += (2 * i - 1) ** 2
    countDelCube = (2 * i - 1) ** 3 - countCube
    print(countDelCube, end=" ")