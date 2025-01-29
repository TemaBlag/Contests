nmq = input().split()
n = int(nmq[0])
m = int(nmq[1])
q = int(nmq[2])
labyrinth = []
for i in range(n):
    values = input().split()
    for j, elem in enumerate(values):
        values[j] = int(elem)
    labyrinth.append(values)
result = []
for i in range(q):
    count = 0
    trial = input().split()
    x = int(trial[0]) - 1
    y = int(trial[1]) - 1
    k = int(trial[2])
    for col in range(n):
        if abs(labyrinth[col][y] - labyrinth[x][y]) <= k:
            count += 1
    for row in range(m):
        if abs(labyrinth[x][row] - labyrinth[x][y]) <= k:
            count += 1
    result.append(count - 2)

for k in range(len(result)):
    print(result[k])