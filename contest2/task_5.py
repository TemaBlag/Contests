countHerd = int(input())
numA = 0
numB = 0
numC = 0
numHorses = 0
ugliness = 0
horses = []
buf = []
while countHerd:
    herd = input()
    lenHerd = len(herd)
    a = herd.count("a")
    b = herd.count("b")
    c = herd.count("c")
    numA += a
    numB += b
    numC += c
    horses.append([a, b, c])
    countHerd -= 1
numHorses = numA + numB + numC
ugliness = max(numA, numB, numC) - min(numA, numB, numC)
for p in range(3):
    l = len(horses)
    while l:
        x0 = horses[0][0]
        y0 = horses[0][1]
        z0 = horses[0][2]
        ugliness0 = max(x0, y0, z0) - min(x0, y0, z0)
        numIn = [0]
        for i in range(1, l):
            x = horses[i][0]
            y = horses[i][1]
            z = horses[i][2]
            newUgliness = max(x0 + x, y0 + y, z0 + z) - min(x0 + x, y0 + y, z0 + z)
            if newUgliness <= ugliness0:
                x0 += x
                y0 += y
                z0 += z
                ugliness0 = newUgliness
                numIn.append(i)
        buf.append([x0, y0, z0])
        for i in range(len(numIn)):
            horses.pop(i)
        l = len(horses)
    horses = buf
    buf = []
for i in range(len(horses)):
    a = horses[i][0]
    b = horses[i][1]
    c = horses[i][2]
    count = a + b + c
    ugl = max(a, b, c) - min(a, b, c)
    if ugl < ugliness:
        numHorses = count
        ugliness = ugl
    elif ugl == ugliness and count > numHorses:
        numHorses = count
        ugliness = ugl
print(numHorses)

"""
def max_horse_power(n, herds):
    MAX_UGLINESS = 1000
    MAX_HORSES = 510

    # Инициализация массива dp
    dp = [[[0] * (MAX_HORSES) for _ in range(MAX_HORSES)] for _ in range(MAX_UGLINESS)]

    for herd in herds:
        # Подсчет лошадей каждого типа в табуне
        a = herd.count('a')
        b = herd.count('b')
        c = herd.count('c')

        # Обновление массива dp
        for i in range(MAX_UGLINESS - 1, -1, -1):
            for j in range(MAX_HORSES - a - 1, -1, -1):
                for k in range(MAX_HORSES - b - 1, -1, -1):
                    ugliness = i + max(a - j, 0) + max(b - k, 0) + max(c - (a + b + c - j - k), 0)
                    dp[ugliness][j + a][k + b] = max(dp[ugliness][j + a][k + b], dp[i][j][k] + a + b + c)

    # Поиск ответа на основе массива dp
    for i in range(MAX_UGLINESS):
        max_power = max(dp[i][j][k] for j in range(MAX_HORSES) for k in range(MAX_HORSES))
        if max_power > 0:
            return max_power

    return -1

# Чтение входных данных
n = int(input().strip())
herds = [input().strip() for _ in range(n)]

# Вывод максимальной силы при минимальном уродстве
print(max_horse_power(n, herds))
"""