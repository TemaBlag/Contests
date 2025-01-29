n, m = [int(x) for x in input().split()] # два значения n и m
password = input() # сам пароль
letters = {} # словарь
result = 0
for let in password:
    letters[let] = letters.get(let, 0) + 1 # заполнение словаря подсчётом букв
letters = dict(sorted(letters.items(), key=lambda item: item[1])) # сортировка словаря
for key, val in letters.items():
    if val > m:
        result += 1 # подсчёт букв, которые остаются
    m -= val
print(result)